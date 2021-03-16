//
//  CreateOrderPresenter.swift
//  CleanStore
//
//  Created by 김예랑 on 2021/03/13.
//  Copyright (c) 2021 ___ORGANIZATIONNAME___. All rights reserved.
//
//  This file was generated by the Clean Swift Xcode Templates so
//  you can apply clean architecture to your iOS and Mac projects,
//  see http://clean-swift.com
//

import UIKit

protocol CreateOrderPresentationLogic {
  func presentSomething(response: CreateOrder.Something.Response)
}

class CreateOrderPresenter: CreateOrderPresentationLogic {
  weak var viewController: CreateOrderDisplayLogic?
  
  // MARK: Do something
  
  func presentSomething(response: CreateOrder.Something.Response) {
    let viewModel = CreateOrder.Something.ViewModel()
    viewController?.displaySomething(viewModel: viewModel)
  }
}
