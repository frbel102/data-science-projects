import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  array = np.array(list)
  mean = np.mean(array)
  
  std = np.std(array)
  var = np.var(array)
  min = np.min(array)
  max = np.max(array)
  sum = np.sum(array)
  newArray = array.reshape(3,3)
  meanOfRow0 = np.mean(newArray[0,:])
  meanOfRow1 = np.mean(newArray[1,:])
  meanOfRow2 = np.mean(newArray[2,:])
  meanOfcolumn0 = np.mean(newArray[:,0])
  meanOfcolumn1 = np.mean(newArray[:,1])
  meanOfcolumn2 = np.mean(newArray[:,2])
  minOfRow0 = np.min(newArray[0,:])
  minOfRow1 = np.min(newArray[1,:])
  minOfRow2 = np.min(newArray[2,:])
  minOfcolumn0 = np.min(newArray[:,0])
  minOfcolumn1 = np.min(newArray[:,1])
  minOfcolumn2 = np.min(newArray[:,2])
  maxOfRow0 = np.max(newArray[0,:])
  maxOfRow1 = np.max(newArray[1,:])
  maxOfRow2 = np.max(newArray[2,:])
  maxOfcolumn0 = np.max(newArray[:,0])
  maxOfcolumn1 = np.max(newArray[:,1])
  maxOfcolumn2 = np.max(newArray[:,2])
  stdOfRow0 = np.std(newArray[0,:])
  stdOfRow1 = np.std(newArray[1,:])
  stdOfRow2 = np.std(newArray[2,:])
  stdOfcolumn0 = np.std(newArray[:,0])
  stdOfcolumn1 = np.std(newArray[:,1])
  stdOfcolumn2 = np.std(newArray[:,2])
  varOfRow0 = np.var(newArray[0,:])
  varOfRow1 = np.var(newArray[1,:])
  varOfRow2 = np.var(newArray[2,:])
  varOfcolumn0 = np.var(newArray[:,0])
  varOfcolumn1 = np.var(newArray[:,1])
  varOfcolumn2 = np.var(newArray[:,2])
  sumOfRow0 = np.sum(newArray[0,:])
  sumOfRow1 = np.sum(newArray[1,:])
  sumOfRow2 = np.sum(newArray[2,:])
  sumOfcolumn0 = np.sum(newArray[:,0])
  sumOfcolumn1 = np.sum(newArray[:,1])
  sumOfcolumn2 = np.sum(newArray[:,2])
  listOfMeanRows = [meanOfRow0, meanOfRow1, meanOfRow2]
  listOfMeancolumns = [meanOfcolumn0, meanOfcolumn1, meanOfcolumn2]
  listOfMinRows = [minOfRow0, minOfRow1, minOfRow2]
  listOfMincolumns = [minOfcolumn0, minOfcolumn1, minOfcolumn2]
  listOfMaxRows = [maxOfRow0, maxOfRow1, maxOfRow2]
  listOfMaxcolumns = [maxOfcolumn0, maxOfcolumn1, maxOfcolumn2]
  listOfSumRows = [sumOfRow0, sumOfRow1, sumOfRow2]
  listOfSumcolumns = [sumOfcolumn0, sumOfcolumn1, sumOfcolumn2]
  listOfStdRows = [stdOfRow0, stdOfRow1, stdOfRow2]
  listOfStdcolumns = [stdOfcolumn0, stdOfcolumn1, stdOfcolumn2]
  listOfVarRows = [varOfRow0, varOfRow1, varOfRow2]
  listOfVarcolumns = [varOfcolumn0, varOfcolumn1, varOfcolumn2]
  listOfMean = [listOfMeancolumns, listOfMeanRows, mean]
  listOfMin = [listOfMincolumns, listOfMinRows, min]
  listOfMax = [listOfMaxcolumns, listOfMaxRows, max]
  listOfStd = [listOfStdcolumns, listOfStdRows, std]
  listOfVar = [listOfVarcolumns, listOfVarRows, var]
  listOfSum = [listOfSumcolumns, listOfSumRows, sum]
  calculations = {
    "mean": listOfMean,
    "variance": listOfVar,
    "standard deviation": listOfStd,
    "max": listOfMax,
    "min": listOfMin,
    "sum": listOfSum
  }
  return calculations