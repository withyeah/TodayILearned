//
//  AppDelegate.swift
//  H4XOR News
//
//  Created by 김예랑 on 2020/09/21.
//

import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

//    struct WebView: UIViewRepresentable {
//
//        let urlString: String?
//
//        func makeUIView(context: Context) -> WKWebView {
//            return WKWebView()
//        }
//
//        func updateUIView(_ uiView: WKWebView, context: Context) {
//            if let safeString = urlString {
//                if let url = URL(string: safeString) {
//                    let request = URLRequest(url: url)
//                    uiView.load(request)
//
//                }
//
//            }
//        }
//    }

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        return true
    }

    // MARK: UISceneSession Lifecycle

    func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        // Called when a new scene session is being created.
        // Use this method to select a configuration to create the new scene with.
        return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
    }

    func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
        // Called when the user discards a scene session.
        // If any sessions were discarded while the application was not running, this will be called shortly after application:didFinishLaunchingWithOptions.
        // Use this method to release any resources that were specific to the discarded scenes, as they will not return.
    }


}

