protocol CanFly {
    func fly()
}

extension CanFly {
    func fly() {
        print("The object takes off into the air.")
    }
}

class Bird {
    
    var isFemale = true
    
    func layEgg() {
        if isFemale {
            print("The bird makes new bird")
        }
    }
}

class Eagle: Bird, CanFly {
    
    func soar() {
        print("The eagle glides in the air.")
    }
}


class Penguin: Bird {
    
    func swim() {
        print("THe penguin paddles through the water.")
    }
}

struct FlyingMuseum {
    func flyingDemo(flyingObject: CanFly){
        flyingObject.fly()
    }
}

struct Airplane: CanFly {
}

let myEagle = Eagle()
let myPenguin = Penguin()
let myPlane = Airplane()

let museum = FlyingMuseum()
museum.flyingDemo(flyingObject: myPlane)

myPlane.fly()
