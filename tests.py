from assignment4 import *
import pytest


def test_observed():
    seq="ATTTGGATT"
    k =1
    output=3
    assert output==observed(seq,k)

def test_poss():
    seq="ATTTGGATT"
    k=1
    expected_output=4
    assert output==possilbe(seq,k)

def linguistic_complexity():
    obs=35
    poss=40
    output=.875
    assert output==lingProb(obs,poss)
