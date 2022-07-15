//
//  Services.swift
//  DemoProtoBuf
//
//  Created by Nguyen Quang Hung on 14/07/2022.
//

import Foundation
import Alamofire

class Service {
  static let shared = Service() // 1
  let url = "http://127.0.0.1:5000"
  
  private init() { }
  
  func getCurrentUser(_ completion: @escaping (Contact?) -> ()) { // 2
    let path = "/currentUser"
    AF.request("\(url)\(path)").responseData { response in
        switch response.result {
            case .success(let value):
                let contact = try? Contact(serializedData: value) // 4
                completion(contact)
            case .failure(_):
                break
        }
      }
      completion(nil)
  }
    
    func getSpeakers(_ completion: @escaping (Speakers?) -> ()){
        let path = "/speakers"
        AF.request("\(url)\(path)").responseData { response in
            switch response.result {
                case .success(let value):
                    let speakers = try? Speakers(serializedData: value) // 4
                    
                    completion(speakers)
                case .failure(_):
                    break
            }
        }
        completion(nil)
    }
}
