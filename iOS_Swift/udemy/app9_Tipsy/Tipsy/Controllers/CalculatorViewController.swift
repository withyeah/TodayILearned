//
//  ViewController.swift
//  Tipsy
//
//  Created by Angela Yu on 09/09/2019.
//  Copyright © 2019 The App Brewery. All rights reserved.
//

import UIKit

class CalculatorViewController: UIViewController {

    var tipPercentage = 0.2
    var numberOfPeople = 2.0
    
    var calculatorBrain = CalculatorBrain()
    
    @IBOutlet weak var billTextField: UITextField!
    @IBOutlet weak var zeroPctButton: UIButton!
    @IBOutlet weak var tenPctButton: UIButton!
    @IBOutlet weak var twentyPctButton: UIButton!
    @IBOutlet weak var splitNumberLabel: UILabel!
    

    @IBAction func tipChanged(_ sender: UIButton) {
        
        billTextField.endEditing(true)
        
        let selectedButton = sender.currentTitle!
        if selectedButton == "0%" {
            zeroPctButton.isSelected = true
            tenPctButton.isSelected = false
            twentyPctButton.isSelected = false
            self.tipPercentage = 0.0
        } else if selectedButton == "10%" {
            zeroPctButton.isSelected = false
            tenPctButton.isSelected = true
            twentyPctButton.isSelected = false
            self.tipPercentage = 0.1
        } else {
            zeroPctButton.isSelected = false
            tenPctButton.isSelected = false
            twentyPctButton.isSelected = true
            self.tipPercentage = 0.2
        }
    }
    
    @IBAction func stepperValueChanged(_ sender: UIStepper) {
        numberOfPeople = sender.value
        splitNumberLabel.text = String(format: "%.0f", numberOfPeople)
    }
    
    @IBAction func calculatePressed(_ sender: UIButton) {
        let billTotal = Double(billTextField.text!)!
        
        calculatorBrain.calculateTip(billTotal: billTotal, tipPercentage: tipPercentage, numberOfPeople: numberOfPeople)

        performSegue(withIdentifier: "goToResult", sender: self)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "goToResult" {
            let destinationVC = segue.destination as! ResultsViewController
            destinationVC.calculatedBill = calculatorBrain.getCalculatedBill()
            destinationVC.helperNotice = calculatorBrain.getHelperNotice()
        }
    }

}

