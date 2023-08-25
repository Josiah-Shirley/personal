import random

def main():

    # (term, definition)
    a = ("Reinforcement", "Something that increases the probability of future behavior")
    b = ("Punishment", "Something that decreases the probability of future behavior")
    c = ("Negative reinforcement", "The removal of a stimulus that increases the probability of future behavior")
    d = ("Positive reinforcement", "The addition of a stimulus that increases the probability of future behavior")
    e = ("Conditioned reinforcement", "Something that is reinforcing as the result of being paired with an already reinforcing stimulus")
    f = ("Unconditioned reinforcement", "Something that is naturally reinforcing")
    g = ("Schedules of reinforcement", "System that describes when reinforcement will be delivered")
    h = ("Continuous reinforcement", "Delivering reinforcement every time a target behavior occurs")
    i = ("Intermittent reinforcement", "Only delivering reinforcement after some instances of the target behavior")
    j = ("Fixed-Ratio schedule of reinforcement", "Reinforcement is delivered after a set amount of occurences of the target behavior")
    k = ("Variable-Ratio schedule of reinforcement", "Reinforcement is delivered after a variable amount of occurences of the target behavior")
    l = ("Fixed-Interval schedeule of reinforcement", "Reinforcement is delivered after a set amount of time has passed")
    m = ("Variable-Interval schedule of reinforcement", "Reinforcement is delivered after a variable amount of time has passed")
    n = ("Motivating operation", "Something that augments that value of a reinforcer")
    o = ("Positive punishment", "The addition of a stimulus that decreases the probability of future behavior")
    p = ("Negative punishment", "The removal of a stimulus that decreases the probability of future behavior")
    q = ("Discrete trial training", "A teaching procedure in which learning trials are presented in quick succession, with each trial having a clear beginning and end")
    r = ("The five trials in a DTT series", "Probe trial, prompt trial, transfer trial, distractor trial, and check trial")
    s = ("Natural environment training", "A teaching procedure in which the reinforcing stimulus is within the context of the activity")
    t = ("Generalization", "Occurs when a skill learned in a clinical setting is applied in similar situations")
    u = ("maintainance", "When a skill acquisition or behavior reduction can still be observed long after the skill or behavior is no longer targetted")
    v = ("Task analysis", "Definint a complex task by its objetive sub-behaviors (e.g. washing hands involving several individual behaviors)")
    w = ("Chaining", "Teaching a series of connected behaviors successively by teaching them one at a time")
    x = ("Stimulus transfer", "Fading prompts and this transfering the stimulus control from the prompt to the SD")
    y = ("Prompting", "Giving the learner a hint or assistance in performing a target behavior")
    z = ("Prompt fading", "Reduing the intrusiveness of prompts across multiple trials")
    aa = ("Shaping", "Differentially reinforcing successive approximations of a target behavior")
    ab = ("Frequency", "The number of times a behavior occurs during a given amount of time")
    ac = ("Rate", "The number of times a behavior occurs per some unit of time (Think velocity)")
    ad = ("Permanent product", "The result of a behavior that can be observed after the behavior has occured")
    ae = ("Latency", "The time between administration of the SD and the beginning of the behavioral response")
    af = ("Inter response time", "The time between instances of a target behavior")
    ag = ("Duration", "The time over which a behavior occurs")
    ah = ("Discontinuous Measurement", "Not measuring every occurence of a behavior but rather and estimate of occurences of a behavior over time")
    ai = ("continuous measurement", "Measuring every instance of a behavioral occurence")
    aj = ("Whole interval recording", "A type of discontinuous measurement wherein it is recorded whether or not a behavior occurs for an entire interval or not")
    ak = ("Partial interval recording", "A type of discontinuous recording wherein it is recorded whether or not a behavior occurs at all during an interval")
    al = ("Momentary time sampling", "Recording whether a behavior is occuring at the end of each interval")
    am = ("The four functions of behavior", "Attention, Tangible, Escape/Avoidance, Automatic")
    an = ("automatic reinforcement", "Something that is reinforcing as a result of a physical response to stumuli")
    ao = ("Tangible reinforcement", "Reinforcement in the form of gaining access to some item or activity")
    ap = ("Attention reinforcement", "Reinforcement in the form of social attention")
    aq = ("Escape/avoidance reinforcement", "Reinforcement in the form of not having to continue experiencing or begin experiencing some stimuli")
    ar = ("Escape", "Ceasing the experience of some stimuli")
    # "as" is skipped because it is a reserved word in python.
    at = ("Avoidance", "Preventing the experience of some stimuli")
    au = ("Antecedent", "Stimulus that occurs immediately before a behavior")
    av = ("Behavior", "Anything that a person says or does")
    aw = ("Consequence", "Something that happens immediately after a behavior")
    ax = ("Behavior intervention plan", "A document describing the procedures that are to be used to help the learner decrease their challenging behavior and choose more adaptive replacement behaviors")
    ay = ("Differential reinforcement of other", "Reinforcing when any behavior other than the target behavior occurs")
    az = ("Differential reinforcement of alternate", "Reinforcing when a specific alternative behavior that serves the same function as the target behavior occurs")
    ba = ("Differential reinforcement of incompatible", "reinforcing occurences of a specific behavior that is physically incompatible with the target behavior")
    bb = ("Differential reinforcement of lower", "Reinforcing lower rates or frequencies of a target behavior")
    bc = ("Differential reinforcement of higher", "Reinforcing higher rates or frequencies of a target behavior")
    bd = ("Extinction", "Not providing any reinforcement for a target behavior in the hopes that the behavior will no longer occur")
    be = ("Verbal behavior", "Anything someone does in an attempt to communicate with another person(s)")
    bf = ("Vocal behavior", "Using one's voice to communicate with another person(s)")
    bg = ("Mand", "Using verbal behavior to specify a desired reinforcer")
    bh = ("Tact", "Using verbal behavior to label something in the environment")
    bi = ("Echoic", "Using vocal behavior to repeat vocal behavior")
    bj = ("Intraverbal", "Using vocal behavior in response to outside vocal behavior other than simply repeated what was previously said")
    bk = ("The four verbal operants", "Mand, tact, echoic, intraverbal")
    bl = ("Types of prompts", "Full physical, partial physical, modeling, verbal, gestural, visual")
    bm = ("By recording how long it takes a client to get dressed in the morning, you are taking ________ data", "Duration")
    bn = ("Grading a test is an example of using _______ data", "Permanent product data")
    bo = ("As an RBT, your role in a functional assessment is to...", "Assist in the assessment")
    bp = ("What is the primary role of an RBT", "Implimentation")
    dq = ("By recording the time your client takes between bites of food, you are taking ______ data", "Inter-response time")


    termsAndAnswerTuples = [a,b,c,d,e,f,g,h,i,j,k,l,m,n, o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,\
        ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap,aq,ar,at,au,av,aw,ax,ay,az,ba,bb,bc,bd,be,bf\
        ,bg,bh,bi,bj,bk,bl,bm,bn,bo,bp,dq]

    def askQuestion(n):
        iterator = 0
        print(n, "Questions this time...")
        print("----------------------")
        print("First Question...")
        indexList = random.sample(termsAndAnswerTuples, n)
        for questionTuple in indexList:
            print(questionTuple[0])
            userResponse = input("> ")
            print("Your answer:", userResponse)
            print("Correct answer:", questionTuple[1])
            print("----------------------")
            iterator += 1
            if iterator < n-1:
                print("Next Question...")
            elif iterator == n-1:
                print("Last Question!")

    def randomNumberOfQuestions():
        print("----------------------")
        numQuestions = random.randint(1, 10)
        if numQuestions == 0:
            askQuestion(1)
        else:
            askQuestion(numQuestions)
        print("All done. Good job!")
        print("----------------------")
    
    def setNumberOfQuestions(n):
        print("----------------------")
        askQuestion(n)
        print("All done. Good job!")
        print("----------------------")

    def askUserHowManyQuestions():
        print("How many questions would you like to answer? (Type a number or 'R' for a random number)")
        questionNumResponse = input("> ")
        if type(questionNumResponse) is int:
            setNumberOfQuestions(int(questionNumResponse))
        elif questionNumResponse in ['r', 'R', 'random', "Random"]:
            randomNumberOfQuestions()

    #askUserHowManyQuestions()
    randomNumberOfQuestions()



main()

