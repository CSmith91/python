name = input("Type your name: ")
loss_msg = "Not a valid option. You lose."
print("Well met", name, "to this ultimate quest!")

answer = input(
    "Leaving the tavern at first light, you journey west in search of Lord Havershamfordshire II. Trees keep a distance from the road like royal sentinals, casting their long shadows over you like a cool cloak. You come to a fork in the road. You can go left or right. Left seems like it is more west and the road maintains a better quality stone. To the right, the trees edge closer, with vines sprouting over the road like coiling fingers. Which way would you like to go? ").lower()

if answer == "left":
    q2 = input("You proceed down the road and come to a sturdy bridge over a river. You note an upturned wagon blocking the bridge and crows squawking atop. The river appears shallow, but you don't know how fast the current is moving beneath. You can either cross the bridge or swim the river. Type 'cross' to cross the bridge or 'swim' to swim the river: ")

    if q2  == 'swim':
        print("You step into the cool water, unsure if you can make the swim with your satchel. As you wade deeper into the water, you feel your feet lift off from the muddy pebble riverbed. You glide - drift - rapidly. You try to swim, but alas, the current is too strong. You hear the squawking crows fade to the rush of the water, until you realise you can't breath. Alas, you drowned.")

    elif q2 == 'cross':
        print("You step closer to the wagon and the crows take flight. Something is in that wagon. Something living. You kick the side of the wagon with a tentative foot. A thud comes back. Bang! The door opens, and out comes a zombie! Crivens! It overpowers you and before you know it, you have lost consciousness. Game over.")

    else:
        print(loss_msg)     

elif answer == "right":
    q2 = input("The forest closes in as you venture rightward. You feel the odd branch snag on your cape or brush over the nape of your neck. You stop before a fallen tree that blocks the road entirely. You note the tree has been sawed at the base by man. What would you like to do? Vault the tree, turn back? (jump/return): ")

    if q2  == 'jump':
        print("Leaping over the tree, you catch the glint of steel. Bandits! Alas, you lose.")

    elif q2 == 'return':
        q3 = input("You retrace your steps and return to the tavern. You can either snooze or travel east. (snooze/east): ")
        if q3 == "snooze":
            print("You awake to find Lord Havershamfordshire II awaiting you downstairs. You tell him your urgent message. Huzzah!")
            print("You win!")
        elif q3 == 'east':
            print("On heading east, you realise you forgot your water. You turn back, but get lost and perish. Game over.")
        else:
            print(loss_msg) 
    else:
        print(loss_msg)    

else:
    print(loss_msg) 

print("Thank you for playing", name)