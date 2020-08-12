//
//  CalculatorBrain.swift
//  Tipsy
//
//  Created by 김예랑 on 2020/07/04.
//  Copyright © 2020 The App Brewery. All rights reserved.
//

import Foundation

struct CalculatorBrain {
    
    var tip: Tip?
    
    func getCalculatedBill() -> String {
        return String(tip?.calculatedBill ?? "0.00")
    }
    
    func getHelperNotice() -> String {
        return tip?.helperNotice ?? "No input of total bill."
    }
    
    mutating func calculateTip(billTotal: Double, tipPercentage: Double, numberOfPeople: Double) {
        let billPlusTip = billTotal * (tipPercentage + 1)
        let billPerPerson = Float(billPlusTip / Double(numberOfPeople))
        let calculatedBill = String(format: "%.2f", billPerPerson)
        let helperNotice = "Split between \(numberOfPeople) people, with \(Int(tipPercentage * 100))% tip."
        tip = Tip(calculatedBill: calculatedBill, helperNotice: helperNotice)
    }
}
