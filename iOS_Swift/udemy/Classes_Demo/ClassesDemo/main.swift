
var skeleton1 = Enemy(health: 100, attackStrength: 10)
var skeleton2 = skeleton1

skeleton1.takeDamage(amount: 10)
skeleton1.takeDamage(amount: 10)

skeleton2.takeDamage(amount: 10)

print(skeleton1.health) // 80
print(skeleton2.health) // 90
