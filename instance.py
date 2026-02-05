from cursor import Cursor

test_text = """[Verse 1]
I'm offering to you a business proposal
My new weight loss methods are at your disposal
For pennies a day get your college diploma
And miracle pills found to cure melanoma
So tell me if you are a small business owner
Because I am offering free ink and toner
I've got Oxycodone without a prescription
And replica watches with custom inscriptions

[Pre-Chorus]
My name is Wanita, I'm young and I'm lonely
For one hundred dollars in USD only
Get discount Levitra and discount Cialis
I'm here in Nigeria alone in my palace
I need you to save me, I have too much money
The government hates me but I know you love me
I'm desperate and wealthy, I'm single and Christian
You're all I have left and I pray that you'll listen to

[Chorus]
One weird tip discovered by a mom
A weird old tip discovered by a mom
And you can own YourName.Com
And you can own YourName.Com
And you can own YourName.Net
With all the action you are gonna get
With self-help talks on CD-ROM
And one weird tip discovered by a mom
[Verse 2]
Jessica Landon tagged you in a photo
And Danny Malone shared a link on your timeline
And Benjamin Keaton is following you
And your dad commented on a photo you're tagged in
And Christopher Washington wants to be friends
And Michelle Attenborough suggested you like Attenborough Productions
And Lillian Barry invited you to a performance of Tommy

[Pre-Chorus]
My name is Wanita, I'm young and I'm lonely
For one hundred dollars in USD only
Get discount Levitra and discount Cialis
I'm here in Nigeria alone in my palace
I need you to save me, I have too much money
The government hates me, but I know you love me
I'm desperate and wealthy, I'm single and Christian
(It's simple, it's safe, it's a fool-proof system)

[Chorus]
One weird tip discovered by a mom
A weird old tip discovered by a mom
And you can own YourName.Com
And you can own YourName.Com
And you can own YourName.Net
With all the action you are gonna get
With self-help talks on CD-ROM
And one weird tip discovered by a mom
[Outro]
My name is Wanita, I'm young and I'm lonely (One weird trick)
For one-hundred dollars in USD only (Discovered by a mom)
Get discount Levitra and discount Cialis (A weird old tip)
I'm here in Nigeria alone in my palace (Discovered by a mom)
I need you to save me, I have too much money
The government hates me but I know you love me (And you can own)
I'm desperate and wealthy, I'm single and Christian (YourName.Com)
You're all I have left and I pray that you'll listen (And you can own)
My name is Wanita, I'm young and I'm lonely (YourName.Com)
For one-hundred dollars in USD only (And you can own)
Get discount Levitra and discount Cialis (YourName.Net)
I'm here in Nigeria alone in my palace
I need you to save me, I have too much money (With all the action)
The government hates me, but I know you love me (You are gonna get)
I'm desperate and wealthy, I'm single and Christian (With self-help talks)
You're all I have left and I pray that you'll listen (On CD-ROM)
My name is Wanita, I'm young and I'm lonely (And one weird trick)
For one-hundred dollars in USD only (Discovered by a mom)
Get discount Levitra and discount Cialis
I'm here in Nigeria alone in my palace (One weird trick)
I need you to save me, I have too much money (Discovered by a mom)
The government hates me but I know you love me (One weird trick)
I'm desperate and wealthy, I'm single and Christian (Discovered by a mom)
You're all I have left and I- (One-)
"""




class Instance:
    def __init__(self):
        self.cursor = Cursor()
        # self.rows = [[]]
        self.rows = []
        for line in test_text.split("\n"):
            self.rows.append(list(line))

