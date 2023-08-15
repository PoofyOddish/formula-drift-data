from enum import Enum
from pydantic import BaseModel, HttpUrl
from typing import Literal,Union
import datetime

class RunType(str,Enum):
    qualifying = 'Qualifying'
    tandem = 'Tandem'

class EventType(str,Enum):
    pro = 'Pro'
    prospec = 'ProSpec'

class Team(BaseModel):
    """Team model
    Information about
    
    Fields
    ------
    TeamID: int
       
    TeamName: str
     
        
    """
     
    teamID: int
    teamName: str

class Driver(BaseModel):
    """Driver model
    Information about historical drivers
    
    Fields
    ------
    DriverID: int
        Unique ID for drivers
    DriverName: str
        Name of driver
    DriverLocation: str
        Home location of driver
    """
     
    driverID: int
    driverName: str
    driverLocation: str
    driverCountry: str

class Track(BaseModel):
    """Track model
    Information about drift tracks
    
    Fields
    ------
    TrackID: int
        Unique ID for drift tracks
    TrackName: str
        Name of drift track
    TrackCity: str
        City of drift track
    TrackState: str
        State of drift track
    """
     
    trackID: int
    trackName: str
    trackCity: str
    trackState: str

class Season(BaseModel):
    """Season model
    Information about FD season
    
    Fields
    ------
    SeasonID: int
        Unique ID for FD season
    StartDate: date
        Date of first event of season
    EndDate: date
        Date of last event of season
    ProWinner: int
        FK to Pro driver winner
    ProSpecWinner: int
        FK to ProSpec driver winner
    """
     
    seasonID: int
    seasonStartDate: datetime.date
    seasonEndDate: datetime.date
    proWinner: Driver
    proSpecWinner: Driver

class Sponsor(BaseModel):
    """Sponsor model
    Information about historical sponsors
    
    Fields
    ------
    SponsorID: int
        Unique ID for sponsor
    SponsorName: str
        Name of Sponsor
    """
     
    sponsorID: int
    sponsorName: str

class Sponsorship(BaseModel):
    """Sponsorship model
    Information about historical sponsorships
    
    Fields
    ------
    SponsorshipID: int
        Unique ID for driver sponsorships
    DriverID: int
        FK of driver
    SponsorID: int
        FK of sponsor
    StartDate: date
        Rough start date of sponsorship
    EndDate: date
        Rough end date of sponsorship
    """
     
    sponsorshipID: int
    driverID: Driver
    sponsorID: Sponsor
    sponsorshipStartDate: datetime.date
    sponsorshipEndDate: datetime.date

class Car(BaseModel):
    """Car model
    Information about cars
    
    Fields
    ------
    CarID: int
        Unique ID for cars
    CarYear: int
        Year of car make/model
    CarMake: str
        Make of car
    CarModel: str
        Model of car
    Horsepower: int
        Car horsepower
    """
     
    carID: int
    carYear: int
    carMake: str
    carModel: str
    horsepower: int
    tireManufacturer: str

class Event(BaseModel):
    """Event model
    Information about 
    
    Fields
    ------
    TandemID: int
        
    BattleID: int
        
    LeadDriverID: int
        
    """
     
    eventID: int
    trackID: Track
    seasonID: Season
    eventType: EventType
    eventStartDate: datetime.date
    eventEndDate: datetime.date
    eventWinnerID: Driver

class DriverProfile(BaseModel):
    """Driver Profile Model"""
    driverProfileID: int
    driverID: Driver
    teamID: Team
    carID: Car
    profileStartDate: datetime.date
    profileEndDate: datetime.date


#class DriverPerformance(BaseModel):
    """Event model
    Information about 
    
    Fields
    ------
    TandemID: int
        
    BattleID: int
        
    LeadDriverID: int
        
    """
     
   # driverPerformanceID: int
   # eventID: Event
   # driverID: Driver
   # teamID: Team
   # runType: RunType
   # runID: Union[Battle,Qualifying]
   # isWinQualify: bool
   # isCatastrophic: bool
   # carID: Car