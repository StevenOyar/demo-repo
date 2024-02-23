class Car(//parameter pass name to the property
    var name: String, var model: String, var color: String, var doors: Int) { // use of primary constructors
    fun move() {
        println("the car $name car is moving")
    }

    fun stop() {
        println("The car $name  stopped")
    }
}
