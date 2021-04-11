from cspbase import *
from itertools import product
from itertools import permutations
import random



def cartPro(arr1, arr2):
    return list(product(arr1, arr2)) 

def binary(vars_row, values_row,initial_tenner_board,values,bool):
  if bool ==1:
      rowConstraint = {
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8}
      rowConstraint.clear()
      tuples = []
      i=-1
      while i!=9:
        i+=1
        j=i+1
        while j <10:
          cnstrnt = Constraint("",[vars_row[i], vars_row[j]]) 
          for prd in cartPro(values_row[i], values_row[j]):
            if prd[0] != prd[1]:
              tuples.append(prd) 
          cnstrnt.add_satisfying_tuples(tuples)
          rowConstraint[random.randint(0,2**32)]=cnstrnt
          j+=1
          
      rowConstraint = list(rowConstraint.values())
      return rowConstraint


  if bool == 0:
    columnConstraint = []
    sat = []

    length = len(initial_tenner_board[0])
    for i in range(10):
      sc = []
      rangeOfPossibiliteis = []
      for k in range(length):
        sc.append(vars[i+k*10])
        rangeOfPossibiliteis.append(values[i+k*10])
      cnstrnt = Constraint("",sc)  
      tuples = []
      for prd in product(*rangeOfPossibiliteis):
        if sum(prd) != initial_tenner_board[1][i]:
          sat.append(prd)        
        else:
          tuples.append(prd)
      cnstrnt.add_satisfying_tuples(tuples)
      columnConstraint.append(cnstrnt)
    return columnConstraint



def rower(initial_tenner_board, vars, values,bool):

  if bool == 1:
    row_cons ={
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8}
    length = len(initial_tenner_board[0])
    row_cons.clear()
    for i in range(length):
      scope = []
      for j in range(10):
        lengthValues = len(values[i*10+j]) 
        if lengthValues != 1:
          scope.append(vars[i*10+j])
          index = i*10+j

      if(len(scope) == 0):
        continue
      cnstrnt = Constraint("",scope)
      sat_tuples = []
      for t in permutations(*[values[index]]):

          sat_tuples.append(t)
      cnstrnt.add_satisfying_tuples(sat_tuples)
      row_cons[random.randint(0,2**32)]=cnstrnt

    row_cons = list(row_cons.values())
    return row_cons

  if bool == 0:
    column_cons = []
    length = len(initial_tenner_board[0])
    for i in range(10):
      scope = []
      possibilities = []
      for j in range(length):
        scope.append(vars[j*10+i])
        possibilities.append(values[j*10+i])
      cnstrnt = Constraint("",scope)  
      sat_tuples = []
      for t in product(*possibilities):
        if sum(t) == initial_tenner_board[1][i]:
          sat_tuples.append(t)
      cnstrnt.add_satisfying_tuples(sat_tuples)
      column_cons.append(cnstrnt)
    return column_cons



def tenner_csp_model_1(initial_tenner_board):

  var_dic = {
      "Zero": 0,
    "One": 1,
    "Two": 2}
  vars = {}
  values = {}
  length =len(initial_tenner_board[0])
  for i in range(length):
    dom = {
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8,
    "Nine": 9
    }


    domTwo = {
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8,
    "Nine": 9
    }
    
    j=-1
    while j!=length-1:
      j+=1
      if initial_tenner_board[0][i][j] != -1:
        domTwo = {key:val for key, val in domTwo.items() if val != (initial_tenner_board[0][i][j])}

    domTwo = list(domTwo.values())
    dom = list(dom.values())
    var_dic.clear()
    for j in range(10):
      if initial_tenner_board[0][i][j] == -1:
        vars[random.randint(0,2**32)]=(Variable("", dom))
        values[random.randint(0,2**32)]=(domTwo)
      else:
        vars[random.randint(0,2**32)]=(Variable("", [initial_tenner_board[0][i][j]]))
        values[random.randint(0,2**32)]=([initial_tenner_board[0][i][j]])

  cntraint = []
  values = list(values.values())
  vars = list(vars.values())

  length = len(initial_tenner_board[0])
  scope= {
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8}

  possibilities= {
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8}

  inds = {}
  scope = list(scope.values())
  possibilities = list(possibilities.values())
  inds.clear()
  for i in range(length-1):
    for j in range(10):
      if j != 0:
        inds[random.randint(0,2**32)]=([[i,j], [i+1,j-1]])
      if j != 9:
        inds[random.randint(0,2**32)]=([[i,j], [i+1,j+1]])

      inds[random.randint(0,2**32)]=([[i,j], [i+1,j]]) 

    


  inds = list(inds.values())
  for i in range(len(inds)):
    scope.clear()
    scope = [vars[inds[i][0][0]*10+inds[i][0][1]], vars[inds[i][1][0]*10+inds[i][1][1]]]
    possibilities.clear()
    possibilities = [values[inds[i][0][0]*10+inds[i][0][1]], values[inds[i][1][0]*10+inds[i][1][1]]]
    cnstrnt = Constraint(("", inds[i][1]),scope)  
    sat_tuples = []
    for t in product(*possibilities):
      if t[0] != t[1]:
        sat_tuples.append(t)
    cnstrnt.add_satisfying_tuples(sat_tuples)
    cntraint.append(cnstrnt)

  i=-1

  while i!=length-1:
    i+=1
    cntraint = cntraint + binary(vars[i*10:i*10+10], values[i*10:i*10+10],initial_tenner_board,values,1)
  cntraint = cntraint + rower(initial_tenner_board, vars, values,0)
  j=-1
  while j!=length-1:
    j+=1
    var_dic[random.randint(0,2**32)] = vars[10*j:10*j+10]
  csp = CSP("", vars)
  for c in cntraint:
    csp.add_constraint(c)

  var_dic = list(var_dic.values())
  return csp, var_dic

def tenner_csp_model_2(initial_tenner_board):
  vrbs = {}
  val = {}
  varArray = []
  length = len(initial_tenner_board[0])

  i=-1
  while i!=length-1:
    i+=1
    domain_One = {
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8,
    "Nine": 9
    }
    domain_Two = {
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8,
    "Nine": 9
    }

    j=-1
    while j!=9:
      j+=1
      if initial_tenner_board[0][i][j] != -1:
        domain_Two = {key:val for key, val in domain_Two.items() if val != (initial_tenner_board[0][i][j])}
    k=-1
    domain_Two = list(domain_Two.values())
    domain_One = list(domain_One.values())
    while k!=9:
      k+=1
      if initial_tenner_board[0][i][k] == -1:
        vrbs[random.randint(0,2**32)]=(Variable("", domain_One))
        val[random.randint(0,2**32)]=domain_Two
      else:
        vrbs[random.randint(0,2**32)]=(Variable("", [initial_tenner_board[0][i][k]]))
        val[random.randint(0,2**32)] = ([initial_tenner_board[0][i][k]])

  cnstraint = []
  vrbs = list(vrbs.values())
  val = list(val.values())
  contiguous_cons = []
  length = len(initial_tenner_board[0])
  scope= {
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8}
  varArray = {}
  possibilities= {
      "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
        "Four": 4,
    "Five": 5,
    "Six": 6,
        "Seven": 7,
    "Eight": 8}

  inds = {}
  scope = list(scope.values())
  possibilities = list(possibilities.values())
  inds.clear()
  for i in range(length-1):
    for j in range(10):
      if j != 0:
        inds[random.randint(0,2**32)]=([[i,j], [i+1,j-1]])
      if j != 9:
        inds[random.randint(0,2**32)]=([[i,j], [i+1,j+1]])

      inds[random.randint(0,2**32)]=([[i,j], [i+1,j]]) 

    


  inds = list(inds.values())
  for i in range(len(inds)):
    scope.clear()
    scope = [vrbs[inds[i][0][0]*10+inds[i][0][1]], vrbs[inds[i][1][0]*10+inds[i][1][1]]]
    possibilities.clear()
    possibilities = [val[inds[i][0][0]*10+inds[i][0][1]], val[inds[i][1][0]*10+inds[i][1][1]]]
    cnstrnt = Constraint(("", inds[i][1]),scope)  
    sat_tuples = []
    for t in product(*possibilities):
      if t[0] != t[1]:
        sat_tuples.append(t)
    cnstrnt.add_satisfying_tuples(sat_tuples)
    contiguous_cons.append(cnstrnt)

  cnstraint += contiguous_cons
  cnstraint += rower(initial_tenner_board, vrbs, val,1)
  cnstraint += rower(initial_tenner_board, vrbs, val,0)

  l=-1
  while l!=length-1:
    l+=1
    varArray[random.randint(0,2**32)]=(vrbs[10*l:10*l+10])
  csp = CSP("", vrbs)
  for c in cnstraint:
    csp.add_constraint(c)
  varArray = list(varArray.values())
  return csp, varArray