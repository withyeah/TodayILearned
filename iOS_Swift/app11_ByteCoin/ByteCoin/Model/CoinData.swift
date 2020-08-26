//
//  CoinData.swift
//  ByteCoin
//
//  Created by 김예랑 on 2020/08/26.
//  Copyright © 2020 The App Brewery. All rights reserved.
//

import Foundation

struct CoinData: Decodable{
    let asset_id_quote: String
    let rate: Double
}
