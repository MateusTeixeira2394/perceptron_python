from Tkinter import *
import random
import pdb


def readFile(name):
    file = open(name)
    lines=[]
    for line in file:
        lines.append(line.rstrip().split(","))
    return lines

def makeWeights(count):
    weights = []
    for i in range(0,count):
        weights.append(round(random.uniform(1,0),2))
    return weights

def functiony(u):
    if u >= 0:
        return 1
    else:
        return -1


def train(table,weights,n,iteration):
    print "*****************************"
    print "**        Training         **"
    print "*****************************"
    unprepared = True

    while(unprepared):
        fault = len(table)

        for i in range(0,len(table)):
            iteration = iteration + 1
            vector = table[i]
            d_vector = float(vector[-1])
            u_vector = weights[0]*-1

            for j in range(0,len(vector)-1):
                u_vector = u_vector + float(vector[j])*weights[j+1]

            y_vector = functiony(u_vector)

            weights[0] = weights[0] + n*(d_vector-y_vector)*-1

            for z in range(1,len(weights)):
                weights[z] = weights[z] + n*(d_vector-y_vector)*float(vector[z-1])

            print "Iteration: "+str(iteration)
            print vector
            print "Response: "+str(y_vector)
            print weights
            print "-----------------------------------"

            if d_vector == y_vector:
                fault = fault - 1

        if fault == 0:
            unprepared = False
        else:
            unprepared = True

    return [weights,iteration]


def test(weights,test_table):
    print "***************************"
    print "**        Testing         **"
    print "***************************"
    iteration = 0
    for i in range(0,len(test_table)):
        vector = test_table[i]
        u_vector = weights[0]*-1

        for z in range(0,len(vector)-1):
            u_vector = u_vector + float(vector[z])*weights[z+1]

        y_vector = functiony(u_vector)

        iteration = iteration + 1

        print iteration
        print vector
        print "Response: "+str(y_vector)
        print "-----------------------------------"

def import_csv_to_train():
    return readFile('csv_treino.txt')

def import_csv_to_test():
    return readFile('csv_teste.txt')


print ">>>>>>>>>>> Perceptron <<<<<<<<<<<<<"
print ""

iteration = 0

n = 0.01
table = import_csv_to_train()
test_table = import_csv_to_test()

weights = makeWeights(len(table[0]))

trained = train(table,weights,n,iteration)

test(weights,test_table)


# GUI python

# janela = Tk()
# janela.title("Perceptron")
# janela.geometry("600x400")
#
#
# ed = Entry(janela)
# ed.place(x=10,y=50)
#
# btn = Button(janela, width=20,text="Importar",command=printar)
# btn.place(x=10,y=10)
#
# btn_sair = Button(janela, width=20,text="sair",command=sair)
# btn_sair.place(x=200,y=10)
#
# lb = Label(janela,text="")
# lb.place(x=10,y=100)
#
# janela.mainloop()
