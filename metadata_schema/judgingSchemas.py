from enum import Enum
from pydantic import BaseModel, HttpUrl
from typing import Literal,Union
import datetime
from driverSchemas import Driver


class Judge(BaseModel):
    """Judge model
    Information about historical judges
    
    Fields
    ------
    JudgeID: int
        Unique ID for judges
    JudgeName: str
        Name of judge
    JudgeCountry: str
        Country of judge
    """
     
    judgeID: int
    judgeName: str
    judgeCountry: str

class JudgeCall(BaseModel):
    """Judge call model
    Information about judge calls
    
    Fields
    ------
    JudgeCallID: int
        
    Judge1Call: str
        
    Judge2Call: str
        
    Judge3Call: str

    Judge1: int
        
    Judge2: int
        
    Judge3: int

    VideoRef: HttpUrl

    IsContested: bool

    Notes: str
        
        
    """
     
    judgeCallID: int
    judge1Call: Union[Literal['OMT'],Driver]
    judge2Call: Union[Literal['OMT'],Driver]
    judge3Call: Union[Literal['OMT'],Driver]
    judge1: Judge
    judge2: Judge
    judge3: Judge
    judgingVideoRef: HttpUrl
    isProtest: bool
    notes: str
