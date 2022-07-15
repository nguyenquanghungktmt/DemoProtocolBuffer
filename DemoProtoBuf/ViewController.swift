//
//  ViewController.swift
//  DemoProtoBuf
//
//  Created by Nguyen Quang Hung on 14/07/2022.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var textView: UITextView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
//        fetchDataUser()
        
        demoEncode()
    }

    func fetchDataUser() {
        Service.shared.getSpeakers { speakers in
            if let speakers = speakers {
                self.textView.text = speakers.textFormatString()
            }
        }
    }
    
    func demoEncode(){
//        var salary = Salary()
//        salary.a = 147852
        
        var staff = Staff()
        staff.c.a = 147852
        
        print(staff.textFormatString())
        print("\(staff.textFormatString().count) bytes")
        
        do {
            let data : Data = try staff.serializedData()
            print(data)
            print(data.hexEncodedString(options: .upperCase))
        }catch {
            
        }
    }
}

extension Data {
    struct HexEncodingOptions: OptionSet {
        let rawValue: Int
        static let upperCase = HexEncodingOptions(rawValue: 1 << 0)
    }

    func hexEncodedString(options: HexEncodingOptions = []) -> String {
        let format = options.contains(.upperCase) ? "%02hhX" : "%02hhx"
        return self.map { String(format: format, $0) }.joined()
    }
}
extension Data {
    private static let hexAlphabet = Array("0123456789abcdef".unicodeScalars)
    func hexStringEncoded() -> String {
        String(reduce(into: "".unicodeScalars) { result, value in
            result.append(Self.hexAlphabet[Int(value / 0x10)])
            result.append(Self.hexAlphabet[Int(value % 0x10)])
        })
    }
}
