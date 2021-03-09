//
//  ViewController.swift
//  ConstraintLayoutInCode
//
//  Created by 김예랑 on 2021/03/09.
//

import UIKit

class ViewController: UIViewController {

    private let myView: UIView = {
        let myView = UIView()
        myView.translatesAutoresizingMaskIntoConstraints = false
        myView.backgroundColor = .link
        return myView
    }()
    
    private let secondView: UIView = {
        let myView = UIView()
        myView.translatesAutoresizingMaskIntoConstraints = false
        myView.backgroundColor = .systemRed
        return myView
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(myView)
        myView.addSubview(secondView)
        addConstraints()
    }

    private func addConstraints() {
        var constraints = [NSLayoutConstraint]()
        
        // Add constraints
        constraints.append(myView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor))
        constraints.append(myView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor))
        constraints.append(myView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor))
        constraints.append(myView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor))
        
        constraints.append(secondView.widthAnchor.constraint(equalTo: myView.widthAnchor,
                                                             multiplier: 0.5))
        constraints.append(secondView.heightAnchor.constraint(equalTo: myView.heightAnchor,
                                                              multiplier: 0.5))
        constraints.append(secondView.centerYAnchor.constraint(equalTo: myView.centerYAnchor))
        constraints.append(secondView.centerXAnchor.constraint(equalTo: myView.centerXAnchor))
        
        
        // Activate (applying)
        NSLayoutConstraint.activate(constraints)
    }

}

