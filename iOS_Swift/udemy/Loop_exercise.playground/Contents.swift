import UIKit

class Assignment {
    
    
    func fibonacci(_ n: Int) {
    
    //Write your code here.
        var fiboArray: Array = [0, 1]
        for i in 2..<n {
            fiboArray.append(fiboArray[i-2] + fiboArray[i-1])
        }
        print(fiboArray)
    }
    
}


