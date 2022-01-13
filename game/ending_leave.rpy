label ending_leave:

    scene house evening with fade
    with Pause(2)

    show mom neutral at left

    m "... So you decided to Leave?"

    pc "Yeah… Yeah I think I’m going to Leave."

    m "Oh this is so wonderful [yn]! You’ll go out and see the Library and find what you love!"

    m "Just… promise to visit sometimes? I’ll miss you."

    pc "Of course, Mom."

    m "We get you all set up tomorrow."

    m "Anyway, write down your decision and go tell Harper!"

    "[yn] writes \'Leave\' on a piece of paper."

    show town center evening with fade

    show harper neutral at middle
    with Pause(2)

    h "...Took you a while, huh."

    h "…Have you decided?"

    pc "Yeah."

    h "Well, I’ll hand you my note and you hand me yours."

    "You hand Harper the note reading \'Leave\'"

    "Harper hands you a note, folded in half."

    if stay > leave:
        call ending_leave_stay
    else:
        call ending_leave_leave

    return

label ending_leave_stay:

    "You open the note. In shaky handwriting, the word \'Stay\' is written."

    $ renpy.pause(delay=1)

    h "...Oh. I."

    h "I’ll… I’ll miss you, [yn]."

    h "I can’t believe you’re leaving. I just, I’m.. I’m sorry."

    pc "Harper… I… I’ve known you for all my life."

    pc "I’m not going to forget about you, you know that right?"

    h "Yeah I just… I thought we’d stay here together."

    h "… I guess it’s what’s best. It just doesn’t feel like that."

    pc "Yeah. I… I wanted you to come with me but… it wouldn’t be what’s best for you."

    pc "I’ll come and visit from time to time."

    h "Yeah… Yeah."

    h "Why are we standing around being sad? This should be happy!"

    h "You’re going to go and see the Library, and find your place!"

    pc "Yeah! And you’ve already found your place!"

    pc "Come on over for dinner tonight Harper, we’ll celebrate!"

    scene black

    show text "[yn]: Leave \nHarper: Stay" with fade
    with Pause(3)

    return

label ending_leave_leave:

    "You open the note. In shaky handwriting, the word \'Leave\' is written."

    $ renpy.pause(delay=1)

    h "YES!! YOU’RE LEAVING WITH ME!!"

    h "I’m… I’m really glad."

    h "Obviously like I’d support you if you’d Stayed, but… I’d miss you."

    h "I was worried you’d Stay and I’d be going out into the Library alone."

    pc "I was worried you’d Stay!"

    h "Haha, oh, I…"

    h "I’m glad [yn]."

    pc "Yeah… We’ll get to explore the Library!"

    show harper neutral at right

    show mom at left

    m "Harper! Are you also Leaving?"

    h "Yes!"

    m "Oh, that's just wonderful! I'm so glad."

    m "Come on over for dinner tonight, Harper! We'll celebrate!"

    scene black

    show text "[yn]: Leave \nHarper: Leave" with fade
    with Pause(3)

    return
