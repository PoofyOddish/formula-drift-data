from enum import Enum
from pydantic import BaseModel, HttpUrl
from typing import Literal,Union
import datetime
from driverSchemas import Driver
from judgingSchemas import JudgeCall

class Qualifying(BaseModel):
    """Qualifying model
    Information about 
    
    Fields
    ------
    TandemID: int
        
    BattleID: int
        
    LeadDriverID: int
        
    """
     
    qualifyingID: int
    qualifyingScore: float
    xFactorScore: float
    isIncomplete: int
    isCrash: bool
    qualifyingVideoRef: HttpUrl
    isQualify: bool
    isCatastrophic: bool
    driverID: Driver

class Battle(BaseModel):
    """Battle model
    Information about 
    
    Fields
    ------
    BattleID: int
        
    WinnerID: int
        
    JudgeCallID: int
        
    """
     
    battleID: int
    battleWinnerID: Driver
    judgeCallID: JudgeCall

class Tandem(BaseModel):
    """Tandem model
    Information about 
    
    Fields
    ------
    TandemID: int
        
    BattleID: int
        
    LeadDriverID: int
        
    """
     
    tandemID: int
    battleID: Battle
    leadDriverID: Driver
    chaseDriverID: Driver
    leadIncomplete: bool
    chaseIncomplete: bool
    tandemVideoRef: HttpUrl
    isContact: bool
    leadCatastrophic: bool
    chaseCatastrophic: bool