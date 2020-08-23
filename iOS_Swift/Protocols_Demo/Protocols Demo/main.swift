protocol CanFly {
    
    func fly()
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
    
    func fly() {
        print("The eagle flies.")
    }
    
    
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
    
    func fly() {
        print("The airplane lifts off into the air.")
    }
}

let myEagle = Eagle()
let myPenguin = Penguin()
let myPlane = Airplane()

let museum = FlyingMuseum()
museum.flyingDemo(flyingObject: myPlane)
