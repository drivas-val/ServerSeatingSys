from tkinter import *
from tkinter.ttk import Separator, Style
import numpy as np
import tkinter.messagebox

#Start Tkinter
root = Tk()
root.title("Server Sys")

#Num of sections question label
sectionLabel = Label(root, text="How many sections are there?")
sectionLabel.grid(row=0, column=0)

#Entry for num of sections
sectionAnswer = Entry(root)
sectionAnswer.grid(row=1, column=0, columnspan=2, sticky= "w")

#global lists 
seatedList = []
finishButtonList = []

#firstQ Counter
global fQ
fQ = 0

#Function for num of sections button
def sButtonSubmit():
    global sections, tablesEntry, tEntries, tLabels, tableQuestion, submitTable

    #Clears screen --> "sections" set to num of sections
    sections = int(sectionAnswer.get())
    sectionLabel.grid_forget()
    sectionAnswer.grid_forget()
    submitSection.grid_forget()
    sectionAnswer.delete(0,END)

    #Creates questionaire for num of tables in each section
    tableQuestion = Label(root, text="How many tables are in each section?")
    tableQuestion.grid(row=0, column=0, sticky="w")
    tLabels = []
    tEntries = []
    for i in range(int(sections)):
        tablesLabel = Label(root, text= "Section" + " " + str(i+1) + ": ")
        tablesLabel.grid(row= i+1, column=0)
        tLabels.append(tablesLabel)

        tablesEntry = Entry(root)
        tablesEntry.grid(row= i+1, column=1, sticky= "w")
        tEntries.append(tablesEntry)
    
    #Submit button + function call for the number of tables questionaire
    submitTable = Button(root, text="Submit", command= tButtonSubmit)
    submitTable.grid(row=int(sections)+1, column=1)

submitSection = Button(root, text="Submit", command= sButtonSubmit)
submitSection.grid(row=2, column=0, pady= 10)

#Function for num of tables button
def tButtonSubmit():
    #numtables --> index = section, index object = num of tables
    global numTables, sEntries, sLabels, seatQ, submitSeats
    numTables = []
    for entry in tEntries:
        numTables.append(int((entry.get())))

    #clear screen
    tableQuestion.grid_forget()
    for entry in tLabels:
        entry.grid_forget()
    for entry in tEntries:
        entry.grid_forget()
    submitTable.grid_forget()

    #Question label for num of seats
    seatQ = Label(root, text="How many seats are in each section?")
    seatQ.grid(row=0, column=0, sticky="w")

    sLabels = []
    sEntries = []
    sec = 0
    pos = 1

    #create labels for the number of seats per table + entries for answer
    for entry in numTables:
        sec += 1
        tab = 0
        for i in range(entry):
            tab += 1
            seatsLabel = Label(root, text= "S" + str(sec) + "- " + "Table" + str(tab))
            seatsLabel.grid(row= pos, column=0)
            sLabels.append(seatsLabel)

            seatsEntry = Entry(root)
            seatsEntry.grid(row= pos, column=1, sticky= "w")
            sEntries.append(seatsEntry)

            pos += 1

    #Submit button + function call for number of seats (sts)
    submitSeats = Button(root, text="Submit", command= stsButtonSubmit)
    submitSeats.grid(row=pos, column=1)

#function for number of seats button
def stsButtonSubmit():
    global wEntry, waitEntry, waitQ, wLabels, submitWait, numSeats
    #numSeats --> index = table, index object = number of seats
    numSeats = []
    for entry in sEntries:
        numSeats.append(int(entry.get()))

    #clear screen
    seatQ.grid_forget()
    for entry in sLabels:
        entry.grid_forget()
    for entry in sEntries:
        entry.grid_forget()
    submitSeats.grid_forget()

    #questioning label for waiters
    waitQ = Label(root, text="Who is taking care of each section?")
    waitQ.grid(row=0, column=0)

    wLabels = []
    wEntry = []

    #Set a label for each seciton + entry for the waiter taking care for that section
    for i in range(int(sections)):
        waitLabel = Label(root, text= "Section" + " " + str(i+1) + ": ")
        waitLabel.grid(row= i+1, column=0)
        wLabels.append(waitLabel)

        waitEntry = Entry(root)
        waitEntry.grid(row= i+1, column=1, sticky= "w")
        wEntry.append(waitEntry)
    
    #submit button + function call for waiter names for each section
    submitWait = Button(root, text="Submit", command= wButtonSubmit)
    submitWait.grid(row=int(sections)+1, column=1)

    #Creates master list for section, tables, and number of seats

    global master, masterCopy
    master = []
    k = 0
    for i in range(int(sections)):
        newList = []
        for j in range(k, k + numTables[i]):
            k += 1
            newList.append(numSeats[j])
        master.append(newList)
    print(master)

    masterCopy = [x[:] for x in master]


#global for placeholder 
firstClick = True

#When the entry with the placeholder is clicked
def onEntryClick(event):
    global firstClick
    firstClick = True
    if firstClick:
        firstClick = False 
        for entry in partyEntry:
            entry.delete(0, "end") 
            entry.configure(fg="black")

#function for waiter names submit button
def wButtonSubmit():
    global wList, selectWLabel, waiterBtns, swlList
    wList = []
    

    #wList --> index = section, index object = name of the waiter for that section
    for entry in wEntry:
        wList.append(str(entry.get()))

    #clear screen
    waitQ.grid_forget()
    for entry in wLabels:
        entry.grid_forget() 
    for entry in wEntry:
        entry.grid_forget()
    submitWait.grid_forget()

    #Label for waiter selection screen
    swlList = []
    selectWLabel = Label(root, text="Select a Section")
    selectWLabel.grid(row=0, column=0)
    swlList.append(selectWLabel)

    #Option buttons for waiter selection screen
    waiterBtns = []
    for i in range(int(sections)):
        selectWButton = Button(root, text="Section " + str(i+1) + " - " + wList[i], command=lambda i=i: waiterSubmit(i+1))
        selectWButton.grid(row=i+1, column=0)
        waiterBtns.append(selectWButton)

#Function for when a waiter is selected
def waiterSubmit(mySection):
    global partySize, partyEntry, backBtn, mySecLabel, partySize, psButton, separator, inUseLabel, inUseTbls, availableLabel, inUseList, mySec, posCount, firstTime, fQ, zedCount, seatedTitle, separatorr, mySec
    mySec = mySection

    #Clear waiter selection screen
    for entry in swlList:
        entry.grid_forget()
    for entry in waiterBtns:
        entry.grid_forget()

    #poscount = position in grid (row)
    posCount = 0

    #Makes list of available tables in all sections
    available = []
    for num in numSeats:
        available.append((num))

    #Back Button
    backBtn = Button(root, text= "<<", command=backSubmit)
    backBtn.grid(row=posCount, column=0, pady=(0,10), sticky="w")
    posCount += 1

    #Lable header with chosen section + waiter 
    mySecLabel = Label(root, text= "Section " + str(mySection) + " - " + wList[mySection-1])
    mySecLabel.grid(row=posCount, column=0)
    posCount += 1

    #Entry to enter a party that comes in
    partyEntry = []

    partySize = Entry(root, width=14, bd=1, fg="gray")
    partySize.insert(0, "Enter the Party Size")
    partySize.bind("<FocusIn>", onEntryClick)
    partySize.grid(row=posCount, column= 0)
    partyEntry.append(partySize)
    posCount += 1

    #submit button for party-size entry
    psButton = Button(root, text= "Submit", command= psSubmit)
    psButton.grid(row=posCount, column=0)
    posCount += 1

    #Separator between stats and submit button
    separator = Separator(root, orient="horizontal")
    separator.grid(row=posCount,column=0, columnspan=2, pady=(10,10), sticky="we") 
    posCount += 1

    #in use Tables
    inUseList = []
    inUseLblList = []
    inUseLabel = Label(root, text="Tables In Use: ")
    inUseLabel.grid(row=posCount, column=0)
    posCount += 1

    #Find best table with closest # of seats to # of guests
    for index, entry in enumerate(master[mySection-1]):
        if entry == 0:
            inUseList.append(index)
    
    #If in-use list is empty
    if len(inUseList) == 0:
        inUseTbls = Label(root, text= "None")
        inUseTbls.grid(row=posCount, column=0)
        inUseLblList.append(inUseTbls)
        posCount += 1
    else:
        for entry in inUseLblList:
            entry.grid_forget()

    #If in-use list is not empty
    ctr = 0
    for entry in inUseList:
        inUseList[ctr] = str(entry+1)
        ctr += 1 
    
    if len(inUseList) > 0:
        inUseStr = ", ".join(inUseList)
        inUseTbls = Label(root, text= inUseStr)
        inUseTbls.grid(row=posCount, column=0)
        posCount += 1

    #Available Tables
    availableResult = []
    for index, entry in enumerate(master[mySection-1]):
        if entry != 0:
            availableResult.append(index)
    
    ctr = 0
    for entry in availableResult:
        availableResult[ctr] = str(entry+1)
        ctr += 1


    availableStr = ", ".join(availableResult)
    availableLabel = Label(root, text="Tables Available: " + availableStr)
    availableLabel.grid(row=posCount, column= 0)
    posCount += 1

    zedCount = 0 

    #Account for tables already taken
    if len(inUseList) > 0:
        separatorr = Separator(root, orient="horizontal")
        separatorr.grid(row=posCount,column=0, columnspan=2, pady=(10,10), sticky="we") 
        posCount += 1
        seatedTitle = Label(root, text="Seated Tables:") 
        seatedTitle.grid(row=posCount, column=0)
        posCount += 1
        fQ += 1

        for i in inUseList:
            seatedLabel = Label(root, text="Table " + str(inUseList[zedCount]))
            seatedLabel.grid(row=posCount, column=0)
            seatedList.append(seatedLabel)
            finishButton = Button(root, text="Finish", command=lambda i=i: finishSubmit(i))
            finishButton.grid(row=posCount, column=1)
            finishButtonList.append(finishButton)
            posCount += 1
            zedCount += 1
    
    if zedCount == 0:
        posCount += 1

#Function after back button is clicked
def backSubmit():
    global fQ

    if len(inUseList) > 0:
        fQ += 1
    else:
        fQ = 0 
    #clear current screen
    if fQ == 0:
        backBtn.grid_forget()
        mySecLabel.grid_forget()
        partySize.grid_forget()
        psButton.grid_forget()
        separator.grid_forget()
        inUseLabel.grid_forget()
        inUseTbls.grid_forget()
        availableLabel.grid_forget()
    else:
        backBtn.grid_forget()
        mySecLabel.grid_forget()
        partySize.grid_forget()
        psButton.grid_forget()
        separator.grid_forget()
        inUseLabel.grid_forget()
        inUseTbls.grid_forget()
        availableLabel.grid_forget()
        seatedTitle.grid_forget()
        separatorr.grid_forget()
        for entry in seatedList:
            entry.grid_forget()
        for entry in finishButtonList:
            entry.grid_forget()

    #Label for waiter selection screen
    swlList.clear()
    selectWLabel = Label(root, text="Select a Section")
    selectWLabel.grid(row=0, column=0)
    swlList.append(selectWLabel)

    #Option buttons for waiter selection screen
    waiterBtns.clear()
    for i in range(int(sections)):
        selectWButton = Button(root, text="Section " + str(i+1) + " - " + wList[i], command=lambda i=i: waiterSubmit(i+1))
        selectWButton.grid(row=i+1, column=0)
        waiterBtns.append(selectWButton)

#Function after a party-size is submitted
def psSubmit():
    global pSize, posCount, fQ, seatedTitle, seatedLabel, seatedList, separatorr, partyEntry, partySize, backBtn, mySecLabel, psButton, separator, inUseLabel, inUseTbls, availableLabel, inUseList
    pSize = partyEntry[-1].get()

    emptyCheck = 0 
    for index, entry in enumerate(master[mySec-1]):
        if entry != 0:
            emptyCheck += 1

    #Adds taken table and changes page to account for it
    try:
        masterArray = np.array(master[mySec-1])
        next = masterArray[masterArray >= int(pSize)].min()
        tableIndex = master[mySec-1].index(next)
        master[mySec-1][tableIndex] = 0
        partySize.delete(0,END)
    except ValueError:
        tkinter.messagebox.showinfo("Availability Error", "There are no more tables available or there are not enough seats to fit the party!")

    if len(inUseList) > 0:
        fQ += 1
    else:
        fQ = 0 

    #clear current screen
    if fQ == 0:
        backBtn.grid_forget()
        mySecLabel.grid_forget()
        partySize.grid_forget()
        psButton.grid_forget()
        separator.grid_forget()
        inUseLabel.grid_forget()
        inUseTbls.grid_forget()
        availableLabel.grid_forget()
    else:
        backBtn.grid_forget()
        mySecLabel.grid_forget()
        partySize.grid_forget()
        psButton.grid_forget()
        separator.grid_forget()
        inUseLabel.grid_forget()
        inUseTbls.grid_forget()
        availableLabel.grid_forget()
        seatedTitle.grid_forget()
        separatorr.grid_forget()
        for entry in seatedList:
            entry.grid_forget()
        for entry in finishButtonList:
            entry.grid_forget()


    posCount = 0

    #Makes list of available tables in all sections
    available = []
    for num in numSeats:
        available.append((num))

    #Back Button
    backBtn = Button(root, text= "<<", command=backSubmit)
    backBtn.grid(row=posCount, column=0, pady=(0,10), sticky="w")
    posCount += 1

    #Lable header with chosen section + waiter 
    mySecLabel = Label(root, text= "Section " + str(mySec) + " - " + wList[mySec-1])
    mySecLabel.grid(row=posCount, column=0)
    posCount += 1

    #Entry to enter a party that comes in
    partyEntry = []

    partySize = Entry(root, width=14, bd=1, fg="gray")
    partySize.insert(0, "Enter the Party Size")
    partySize.bind("<FocusIn>", onEntryClick)
    partySize.grid(row=posCount, column= 0)
    partyEntry.append(partySize)
    posCount += 1

    #submit button for party-size entry
    psButton = Button(root, text= "Submit", command= psSubmit)
    psButton.grid(row=posCount, column=0)
    posCount += 1

    #Separator between stats and submit button
    separator = Separator(root, orient="horizontal")
    separator.grid(row=posCount,column=0, columnspan=2, pady=(10,10), sticky="we") 
    posCount += 1

    #in use Tables
    inUseList = []
    inUseLblList = []
    inUseLabel = Label(root, text="Tables In Use: ")
    inUseLabel.grid(row=posCount, column=0)
    posCount += 1

    #Find best table with closest # of seats to # of guests
    for index, entry in enumerate(master[mySec-1]):
        if entry == 0:
            inUseList.append(index)
    
    #If in-use list is empty
    if len(inUseList) == 0:
        inUseTbls = Label(root, text= "None")
        inUseTbls.grid(row=posCount, column=0)
        inUseLblList.append(inUseTbls)
        posCount += 1
    else:
        for entry in inUseLblList:
            entry.grid_forget()

    #If in-use list is not empty
    ctr = 0
    for entry in inUseList:
        inUseList[ctr] = str(entry+1)
        ctr += 1 
    
    if len(inUseList) > 0:
        inUseStr = ", ".join(inUseList)
        inUseTbls = Label(root, text= inUseStr)
        inUseTbls.grid(row=posCount, column=0)
        posCount += 1

    #Available Tables
    availableResult = []
    for index, entry in enumerate(master[mySec-1]):
        if entry != 0:
            availableResult.append(index)
    
    ctr = 0
    for entry in availableResult:
        availableResult[ctr] = str(entry+1)
        ctr += 1

    if len(availableResult) == 0:
        availableLabel = Label(root, text="Tables Available: None")
        availableLabel.grid(row=posCount, column=0)
        posCount += 1
    else:
        availableStr = ", ".join(availableResult)
        availableLabel = Label(root, text="Tables Available: " + availableStr)
        availableLabel.grid(row=posCount, column= 0)
        posCount += 1

    zedCount = 0 

    #Account for tables already taken
    if len(inUseList) > 0:
        separatorr = Separator(root, orient="horizontal")
        separatorr.grid(row=posCount, column=0, columnspan=2, pady=(10,10), sticky="we") 
        posCount += 1
        seatedTitle = Label(root, text="Seated Tables:") 
        seatedTitle.grid(row=posCount, column=0)
        posCount += 1
        fQ += 1

        for i in inUseList:
            seatedLabel = Label(root, text="Table " + str(inUseList[zedCount]))
            seatedLabel.grid(row=posCount, column=0)
            seatedList.append(seatedLabel)
            finishButton = Button(root, text="Finish", command=lambda i=i: finishSubmit(int(i)))
            finishButton.grid(row=posCount, column=1)
            finishButtonList.append(finishButton)
            posCount += 1
            zedCount += 1
    
    if zedCount == 0:
        posCount += 1
    
    print(master, '<- master')


#Function for finish button in seated tables
def finishSubmit(myTable):
    global pSize, posCount, fQ, seatedTitle, seatedLabel, seatedList, separatorr, partyEntry, partySize, backBtn, mySecLabel, psButton, separator, inUseLabel, inUseTbls, availableLabel, inUseList
    print(myTable)

    master[int(mySec)-1][int(myTable)-1] = masterCopy[int(mySec)-1][int(myTable)-1]

    #clear current screen
    backBtn.grid_forget()
    mySecLabel.grid_forget()
    partySize.grid_forget()
    psButton.grid_forget()
    separator.grid_forget()
    inUseLabel.grid_forget()
    inUseTbls.grid_forget()
    availableLabel.grid_forget()
    seatedTitle.grid_forget()
    separatorr.grid_forget()
    for entry in seatedList:
        entry.grid_forget()
    for entry in finishButtonList:
        entry.grid_forget()

    posCount = 0 

    #Back Button
    backBtn = Button(root, text= "<<", command=backSubmit)
    backBtn.grid(row=posCount, column=0, pady=(0,10), sticky="w")
    posCount += 1

    #Lable header with chosen section + waiter 
    mySecLabel = Label(root, text= "Section " + str(mySec) + " - " + wList[mySec-1])
    mySecLabel.grid(row=posCount, column=0)
    posCount += 1

    #Entry to enter a party that comes in
    partyEntry = []

    partySize = Entry(root, width=14, bd=1, fg="gray")
    partySize.insert(0, "Enter the Party Size")
    partySize.bind("<FocusIn>", onEntryClick)
    partySize.grid(row=posCount, column= 0)
    partyEntry.append(partySize)
    posCount += 1

    #submit button for party-size entry
    psButton = Button(root, text= "Submit", command= psSubmit)
    psButton.grid(row=posCount, column=0)
    posCount += 1

    #Separator between stats and submit button
    separator = Separator(root, orient="horizontal")
    separator.grid(row=posCount,column=0, columnspan=2, pady=(10,10), sticky="we") 
    posCount += 1

    #in use Tables
    inUseList = []
    inUseLblList = []
    inUseLabel = Label(root, text="Tables In Use: ")
    inUseLabel.grid(row=posCount, column=0)
    posCount += 1

    #Find best table with closest # of seats to # of guests
    for index, entry in enumerate(master[mySec-1]):
        if entry == 0:
            inUseList.append(index)

    #If in-use list is empty
    if len(inUseList) == 0:
        inUseTbls = Label(root, text= "None")
        inUseTbls.grid(row=posCount, column=0)
        inUseLblList.append(inUseTbls)
        posCount += 1
    else:
        for entry in inUseLblList:
            entry.grid_forget()

    #If in-use list is not empty
    ctr = 0
    for entry in inUseList:
        inUseList[ctr] = str(entry+1)
        ctr += 1 
    
    if len(inUseList) > 0:
        inUseStr = ", ".join(inUseList)
        inUseTbls = Label(root, text= inUseStr)
        inUseTbls.grid(row=posCount, column=0)
        posCount += 1

    #Available Tables
    availableResult = []
    for index, entry in enumerate(master[mySec-1]):
        if entry != 0:
            availableResult.append(index)
    
    ctr = 0
    for entry in availableResult:
        availableResult[ctr] = str(entry+1)
        ctr += 1

    if len(availableResult) == 0:
        availableLabel = Label(root, text="Tables Available: None")
        availableLabel.grid(row=posCount, column=0)
        posCount += 1
    else:
        availableStr = ", ".join(availableResult)
        availableLabel = Label(root, text="Tables Available: " + availableStr)
        availableLabel.grid(row=posCount, column= 0)
        posCount += 1

    zedCount = 0 

    #Account for tables already taken
    if len(inUseList) > 0:
        separatorr = Separator(root, orient="horizontal")
        separatorr.grid(row=posCount, column=0, columnspan=2, pady=(10,10), sticky="we") 
        posCount += 1
        seatedTitle = Label(root, text="Seated Tables:") 
        seatedTitle.grid(row=posCount, column=0)
        posCount += 1
        fQ += 1

        for i in inUseList:
            seatedLabel = Label(root, text="Table " + str(inUseList[zedCount]))
            seatedLabel.grid(row=posCount, column=0)
            seatedList.append(seatedLabel)
            finishButton = Button(root, text="Finish", command=lambda i=i: finishSubmit(int(i)))
            finishButton.grid(row=posCount, column=1)
            finishButtonList.append(finishButton)
            posCount += 1
            zedCount += 1
    
    if zedCount == 0:
        posCount += 1

    
# --> End 

root.mainloop()       

"""
Ensure all global vars
Sections --> var = sections
Tables --> list = numTables
Seats --> list = numSeats
Waiter --> list = wList
"""