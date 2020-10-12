# -*- coding: utf-8 -*-
from fonctions import *

def rangerCrêpes( tas ):

  if tas == []:
    return tas 

  plusGrandeCrêpe = numéroPlusGrande( tas )

  if plusGrandeCrêpe == 0:
    return tas[:1] + rangerCrêpes( tas[1:] )

  tasRetourné = retournerTas( tas, plusGrandeCrêpe )
  tasRetourné = retournerTas( tasRetourné, 0 )

  return tasRetourné[:1] + rangerCrêpes( tasRetourné[1:] )


