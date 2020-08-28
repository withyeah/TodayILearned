original = "YJR SMDERT YP YJOD [IXX;R OD YJR DOC VJSTSVYRT MS,R GPT YJR ,PDY VP,,PM LRUNPSTF ;SUPIY"
message  = "THE ANSWER TO THIS      E IS THE     CHARACTER NAME FOR THE MOST COMMON  E OAR  A O T"

key = ['G', 'T', 'P', 'J', 'X', 'D', 'S', '[', ' ', 'R', 'U', 'I', 'O', 'V', 'C', 'E', 'L', 'F', 'Y', ';', ',', 'N', 'M']
val = ['G', 'T', 'P', 'J', 'X', 'D', 'S', '[', ' ', 'R', 'U', 'I', 'O', 'V', 'C', 'E', 'L', 'F', 'Y', ';', ',', 'N', 'M']


# print("".join([val[key.index(x)] for x in original]))

count_char = {}
for char in key:
    count_char[char] = original.count(char)

# print(count_char)

sorted_dict = {k: v for k, v in sorted(count_char.items(), key=lambda item: item[1])}
print(sorted_dict)

# original = original.replace("Y", "A")
# original = original.replace("J", "R")
# original = original.replace("R", "E")
# for i in original:
#     if i != "A" or i != "R" or i != "E":
#         original = original.replace(i, "_")

double_letters = "little, called, better, common, cannot, matter, middle, follow, choose, letter, killed, summer, battle, supply, bottom, passed, button, manner, happen, speech, troops, filled, latter, yellow, dinner, coffee, fellow, tissue, hidden, smooth, pulled, narrow, lesson, missed, cattle, winner, bigger, valley, dollar, suffer, mirror, passes, losses, terror, cotton, summit, cheese, bottle, freely, vessel, sheets, sudden, copper, fallen, differ, gotten, buffer, banner, wheels, rubber, settle, tennis, tunnel, horror, commit, masses, butter, speeds, killer, lesser, rolled, floors, seller, pepper, fitted, soccer, banned, bitter, puzzle, bloody, fossil, skiing, ballot, logged, nodded, rabbit, hammer, barrel, bullet, ballet, hollow, rugged, ladder, bubble, breeds, litter, greens, freeze, collar, sorrow, breeze, cannon, borrow, groove, ribbon, saddle, roller, marrow, shoots, mapped, runner, topped, pollen, sleeve, caller, floods, tonnes, tossed, fuller, dubbed, villas, gallon, hassle, proofs, ripped, pillow, pillar, supper, buffet, billed, ferret, misses, kissed, yelled, barred, dagger, cheeks, puppet, canned, rubbed, paddle, gossip, speedy, fiddle, tapped, coffin, cheers, manned, barren, cutter, cellar, dotted, bosses, tattoo, taller, popped, robbed, sleeps, blooms, wallet, summed, ballad, greedy, tagged, sleepy, rubble, parrot, kennel, kisses, simmer, padded, summon, tipped, rabbis, mammal, begged, reggae, batter, rotten, pinned, fleece, suffix, sweets, lessen, creeks, bidder, kitten, carrot, ridden, mellow, capped, fleets, sweeps, dipped, filler, muzzle, walled, teller, gloomy, toggle, kettle, riddle, midday, bitten, rudder, fodder, nozzle, queens, creepy, funnel, turret, penned, ragged, messed, jammed, hotter, rattle, jagged, spooky, willow, pellet, raffle, ripple, hugged, rigged, hopper, cheesy, stools, zipper, nipple, zipped, pallet, spoons, galley, marred, commas, pitted, gutter, hitter, gunner, culled, pulley, robber, burrow, volley, supple, hopped, ebooks, polled, steers, sallam, rattan, greets, logger, horrid, pebble, groovy, sonnet, steels, bonnet, puddle, beggar, topple, giggle, millet, lessee, potted, hippie, gallop, rapper, bogged, willed, fallow, tosses, crooks, veggie, netted, basses, corral, hellip, pizzas, milled, dogged, creeps, sinner, massed, busses, matted, dammit, potter, jitter, felled, bagged, gettin, hissed, mallet, pegged, massif, patted, tanned, gunned, mutton, sinned, muffin, gutted, rammed, morrow, mussel, wiggle, dazzle, scoops, donned, wedded, mullet, fillet, lagged, juggle, cheery, billet, wobble, bellow, nugget, vassal, batted, cuddly, furrow, breezy, sitter, creeds, bedded, breech, mapper, posses, bubbly, dimmer, sullen, ribbed, vellum, puffed, gasses, dimmed, fanned, tugged, setter, baffle, brooch, buzzer, tiller, legged, tabbed, mosses, steely, digger, tannin, lessor, wetter, messes, sipped, sneeze, fennel, dukkha, bleeds, miller, minnow, wobbly, buddha, putter, huddle, cuddle, doggie, babble, mutter, lapped, kiddie, rotted, gagged, gassed, cupped, cittas, muddle, grooms, nettle, fatter, passwd, bugger, waffle, hemmed, panned, nibble, cheeky, steeds, fellas, bugged, fitter, wallow, bummer, suttas, hobbit, barrio, bobbin, pommel, hippos, russet, hurrah, buzzed, patter, mettle, holler, collie, yuppie, rabble, tallow, brooks, tassel, meddle, callus, peddle, sobbed, kneels, getter, brooms, dulled, maggot, webbed"
double_letters = double_letters.split(", ")
# print(double_letters)
word_list = []
for word in double_letters:
    if word[5] == 'e':
        # for i in word:
        #     if i == 'c' or i == 'o' or i == 'm' or i == 'n':
        #         double_letters.remove(word)
        word_list.append(word)
# print(word_list)

# R까지
oldChars = 'VP,MJSTYTRDEOGPX[UICLF;NGXP[;'
newChars = 'COMNHARTRESWI___________FZOPL'
s = 'apple copyright'
n = original.translate({ ord(x): y for (x, y) in zip(oldChars, newChars) })
# print(n)

key_removed = key
for i in key:
    if i in oldChars:
        key_removed.remove(i)
string = "".join(key_removed)
# print(string)
#