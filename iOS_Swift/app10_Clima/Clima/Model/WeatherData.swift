//
//  WeatherData.swift
//  Clima
//
//  Created by 김예랑 on 2020/08/23.
//  Copyright © 2020 App Brewery. All rights reserved.
//

import Foundation

// Codable = Decodable + Encodable
struct WeatherData: Decodable {
    let name: String
    let main: Main
    let weather: [Weather]
}

struct Main: Decodable {
    let temp: Double
}

struct Weather: Decodable {
    let id: Int
}
