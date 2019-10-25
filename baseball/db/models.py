from sqlalchemy import Boolean, Column, Integer, Numeric, String

from .base import Base


class AllstarFull(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    gameNum = Column(Integer)
    gameID = Column(String, index=True)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    GP = Column(Integer)
    startingPos = Column(Integer)


class Appearances(Base):
    yearID = Column(Integer, index=True)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    playerID = Column(String, index=True)
    G_all = Column(Integer)
    GS = Column(Integer)
    G_batting = Column(Integer)
    G_defense = Column(Integer)
    G_p = Column(Integer)
    G_c = Column(Integer)
    G_1b = Column(Integer)
    G_2b = Column(Integer)
    G_3b = Column(Integer)
    G_ss = Column(Integer)
    G_lf = Column(Integer)
    G_cf = Column(Integer)
    G_rf = Column(Integer)
    G_of = Column(Integer)
    G_dh = Column(Integer)
    G_ph = Column(Integer)
    G_pr = Column(Integer)


class AwardsManagers(Base):
    playerID = Column(String, index=True)
    awardID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    lgID = Column(String, index=True)
    tie = Column(Boolean)
    notes = Column(None) # TODO Manually specify column type


class AwardsPlayers(Base):
    playerID = Column(String, index=True)
    awardID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    lgID = Column(String, index=True)
    tie = Column(Boolean)
    notes = Column(String)


class AwardsShareManagers(Base):
    awardID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    lgID = Column(String, index=True)
    playerID = Column(String, index=True)
    pointsWon = Column(Integer)
    pointsMax = Column(Integer)
    votesFirst = Column(Integer)


class AwardsSharePlayers(Base):
    awardID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    lgID = Column(String, index=True)
    playerID = Column(String, index=True)
    pointsWon = Column(Numeric)
    pointsMax = Column(Integer)
    votesFirst = Column(Numeric)


class Batting(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    stint = Column(Integer)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    G = Column(Integer)
    AB = Column(Integer)
    R = Column(Integer)
    H = Column(Integer)
    _2B = Column("2B", Integer)
    _3B = Column("3B", Integer)
    HR = Column(Integer)
    RBI = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    IBB = Column(Integer)
    HBP = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GIDP = Column(Integer)


class BattingPost(Base):
    yearID = Column(Integer, index=True)
    _round = Column("round", String)
    playerID = Column(String, index=True)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    G = Column(Integer)
    AB = Column(Integer)
    R = Column(Integer)
    H = Column(Integer)
    _2B = Column("2B", Integer)
    _3B = Column("3B", Integer)
    HR = Column(Integer)
    RBI = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    IBB = Column(Integer)
    HBP = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GIDP = Column(Integer)


class CollegePlaying(Base):
    playerID = Column(String, index=True)
    schoolID = Column(String, index=True)
    yearID = Column(Integer, index=True)


class Fielding(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    stint = Column(Integer)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    POS = Column(String)
    G = Column(Integer)
    GS = Column(Integer)
    InnOuts = Column(Integer)
    PO = Column(Integer)
    A = Column(Integer)
    E = Column(Integer)
    DP = Column(Integer)
    PB = Column(Integer)
    WP = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    ZR = Column(Integer)


class FieldingOF(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    stint = Column(Integer)
    Glf = Column(Integer)
    Gcf = Column(Integer)
    Grf = Column(Integer)


class FieldingOFsplit(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    stint = Column(Integer)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    POS = Column(String)
    G = Column(Integer)
    GS = Column(Integer)
    InnOuts = Column(Integer)
    PO = Column(Integer)
    A = Column(Integer)
    E = Column(Integer)
    DP = Column(Integer)
    PB = Column(None) # TODO Manually specify column type
    WP = Column(None) # TODO Manually specify column type
    SB = Column(None) # TODO Manually specify column type
    CS = Column(None) # TODO Manually specify column type
    ZR = Column(None) # TODO Manually specify column type


class FieldingPost(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    _round = Column("round", String)
    POS = Column(String)
    G = Column(Integer)
    GS = Column(Integer)
    InnOuts = Column(Integer)
    PO = Column(Integer)
    A = Column(Integer)
    E = Column(Integer)
    DP = Column(Integer)
    TP = Column(Integer)
    PB = Column(Integer)
    SB = Column(None) # TODO Manually specify column type
    CS = Column(None) # TODO Manually specify column type


class HallOfFame(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    votedBy = Column(String)
    ballots = Column(Integer)
    needed = Column(Integer)
    votes = Column(Integer)
    inducted = Column(Boolean)
    category = Column(String)
    needed_note = Column(String)


class HomeGames(Base):
    year_key = Column("year.key", Integer)
    league_key = Column("league.key", String)
    team_key = Column("team.key", String)
    park_key = Column("park.key", String)
    span_first = Column("span.first", String)
    span_last = Column("span.last", String)
    games = Column(Integer)
    openings = Column(Integer)
    attendance = Column(Integer)


class Managers(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    inseason = Column(Integer)
    G = Column(Integer)
    W = Column(Integer)
    L = Column(Integer)
    rank = Column(Integer)
    plyrMgr = Column(Boolean)


class ManagersHalf(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    inseason = Column(Integer)
    half = Column(Integer)
    G = Column(Integer)
    W = Column(Integer)
    L = Column(Integer)
    rank = Column(Integer)


class Parks(Base):
    park_key = Column("park.key", String)
    park_name = Column("park.name", String)
    park_alias = Column("park.alias", String)
    city = Column(String)
    state = Column(String)
    country = Column(String)


class People(Base):
    playerID = Column(String, index=True)
    birthYear = Column(Integer)
    birthMonth = Column(Integer)
    birthDay = Column(Integer)
    birthCountry = Column(String)
    birthState = Column(String)
    birthCity = Column(String)
    deathYear = Column(Integer)
    deathMonth = Column(Integer)
    deathDay = Column(Integer)
    deathCountry = Column(String)
    deathState = Column(String)
    deathCity = Column(String)
    nameFirst = Column(String)
    nameLast = Column(String)
    nameGiven = Column(String)
    weight = Column(Integer)
    height = Column(Integer)
    bats = Column(String)
    throws = Column(String)
    debut = Column(String)
    finalGame = Column(String)
    retroID = Column(String, index=True)
    bbrefID = Column(String, index=True)


class Pitching(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    stint = Column(Integer)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    W = Column(Integer)
    L = Column(Integer)
    G = Column(Integer)
    GS = Column(Integer)
    CG = Column(Integer)
    SHO = Column(Integer)
    SV = Column(Integer)
    IPouts = Column(Integer)
    H = Column(Integer)
    ER = Column(Integer)
    HR = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    BAOpp = Column(Numeric)
    ERA = Column(Numeric)
    IBB = Column(Integer)
    WP = Column(Integer)
    HBP = Column(Integer)
    BK = Column(Integer)
    BFP = Column(Integer)
    GF = Column(Integer)
    R = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GIDP = Column(Integer)


class PitchingPost(Base):
    playerID = Column(String, index=True)
    yearID = Column(Integer, index=True)
    _round = Column("round", String)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    W = Column(Integer)
    L = Column(Integer)
    G = Column(Integer)
    GS = Column(Integer)
    CG = Column(Integer)
    SHO = Column(Integer)
    SV = Column(Integer)
    IPouts = Column(Integer)
    H = Column(Integer)
    ER = Column(Integer)
    HR = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    BAOpp = Column(Numeric)
    ERA = Column(String)
    IBB = Column(Integer)
    WP = Column(Integer)
    HBP = Column(Integer)
    BK = Column(Integer)
    BFP = Column(Integer)
    GF = Column(Integer)
    R = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GIDP = Column(Integer)


class Salaries(Base):
    yearID = Column(Integer, index=True)
    teamID = Column(String, index=True)
    lgID = Column(String, index=True)
    playerID = Column(String, index=True)
    salary = Column(Integer)


class Schools(Base):
    schoolID = Column(String, index=True)
    name_full = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)


class SeriesPost(Base):
    yearID = Column(Integer, index=True)
    _round = Column("round", String)
    teamIDwinner = Column(String)
    lgIDwinner = Column(String)
    teamIDloser = Column(String)
    lgIDloser = Column(String)
    wins = Column(Integer)
    losses = Column(Integer)
    ties = Column(Integer)


class Teams(Base):
    yearID = Column(Integer, index=True)
    lgID = Column(String, index=True)
    teamID = Column(String, index=True)
    franchID = Column(String, index=True)
    divID = Column(String, index=True)
    Rank = Column(Integer)
    G = Column(Integer)
    Ghome = Column(Integer)
    W = Column(Integer)
    L = Column(Integer)
    DivWin = Column(Boolean)
    WCWin = Column(Boolean)
    LgWin = Column(Boolean)
    WSWin = Column(Boolean)
    R = Column(Integer)
    AB = Column(Integer)
    H = Column(Integer)
    _2B = Column("2B", Integer)
    _3B = Column("3B", Integer)
    HR = Column(Integer)
    BB = Column(Integer)
    SO = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    HBP = Column(Integer)
    SF = Column(Integer)
    RA = Column(Integer)
    ER = Column(Integer)
    ERA = Column(Numeric)
    CG = Column(Integer)
    SHO = Column(Integer)
    SV = Column(Integer)
    IPouts = Column(Integer)
    HA = Column(Integer)
    HRA = Column(Integer)
    BBA = Column(Integer)
    SOA = Column(Integer)
    E = Column(Integer)
    DP = Column(Integer)
    FP = Column(Numeric)
    _name = Column("name", String)
    park = Column(String)
    attendance = Column(Integer)
    BPF = Column(Integer)
    PPF = Column(Integer)
    teamIDBR = Column(String)
    teamIDlahman45 = Column(String)
    teamIDretro = Column(String)


class TeamsFranchises(Base):
    franchID = Column(String, index=True)
    franchName = Column(String)
    active = Column(Boolean)
    NAassoc = Column(String)


class TeamsHalf(Base):
    yearID = Column(Integer, index=True)
    lgID = Column(String, index=True)
    teamID = Column(String, index=True)
    Half = Column(Integer)
    divID = Column(String, index=True)
    DivWin = Column(Boolean)
    Rank = Column(Integer)
    G = Column(Integer)
    W = Column(Integer)
    L = Column(Integer)
