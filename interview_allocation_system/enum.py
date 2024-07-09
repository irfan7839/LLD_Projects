from enum import Enum


class UserType(Enum):
    INTERVIEWEE = 'INTERVIEWEE',
    INTERVIEWER = 'INTERVIEWER'


class InterviewType(Enum):
    JAVA = 'JAVA',
    PYTHON = 'PYTHON',
    LLD = 'LLD',
    DSA = 'DSA'


class InterviewLevel(Enum):
    BASIC = 'BASIC',
    INTERMEDIATE = 'INTERMEDIATE',
    ADVANCE = 'ADVANCE'
