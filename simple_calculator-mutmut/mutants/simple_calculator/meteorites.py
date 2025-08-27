import urllib.request
import json

from simple_calculator.main import SimpleCalculator

URL = ("https://data.nasa.gov/resource/y77d-th95.json")
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class MeteoriteStats:
    def xǁMeteoriteStatsǁget_data__mutmut_orig(self):
        with urllib.request.urlopen(URL) as url:
            return json.loads(url.read().decode())
    def xǁMeteoriteStatsǁget_data__mutmut_1(self):
        with urllib.request.urlopen(None) as url:
            return json.loads(url.read().decode())
    def xǁMeteoriteStatsǁget_data__mutmut_2(self):
        with urllib.request.urlopen(URL) as url:
            return json.loads(None)
    
    xǁMeteoriteStatsǁget_data__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁMeteoriteStatsǁget_data__mutmut_1': xǁMeteoriteStatsǁget_data__mutmut_1, 
        'xǁMeteoriteStatsǁget_data__mutmut_2': xǁMeteoriteStatsǁget_data__mutmut_2
    }
    
    def get_data(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMeteoriteStatsǁget_data__mutmut_orig"), object.__getattribute__(self, "xǁMeteoriteStatsǁget_data__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_data.__signature__ = _mutmut_signature(xǁMeteoriteStatsǁget_data__mutmut_orig)
    xǁMeteoriteStatsǁget_data__mutmut_orig.__name__ = 'xǁMeteoriteStatsǁget_data'

    def xǁMeteoriteStatsǁaverage_mass__mutmut_orig(self, data):
        calculator = SimpleCalculator()

        masses = [float(d['mass']) for d in data if 'mass' in d]

        return calculator.avg(masses)

    def xǁMeteoriteStatsǁaverage_mass__mutmut_1(self, data):
        calculator = None

        masses = [float(d['mass']) for d in data if 'mass' in d]

        return calculator.avg(masses)

    def xǁMeteoriteStatsǁaverage_mass__mutmut_2(self, data):
        calculator = SimpleCalculator()

        masses = None

        return calculator.avg(masses)

    def xǁMeteoriteStatsǁaverage_mass__mutmut_3(self, data):
        calculator = SimpleCalculator()

        masses = [float(None) for d in data if 'mass' in d]

        return calculator.avg(masses)

    def xǁMeteoriteStatsǁaverage_mass__mutmut_4(self, data):
        calculator = SimpleCalculator()

        masses = [float(d['XXmassXX']) for d in data if 'mass' in d]

        return calculator.avg(masses)

    def xǁMeteoriteStatsǁaverage_mass__mutmut_5(self, data):
        calculator = SimpleCalculator()

        masses = [float(d['MASS']) for d in data if 'mass' in d]

        return calculator.avg(masses)

    def xǁMeteoriteStatsǁaverage_mass__mutmut_6(self, data):
        calculator = SimpleCalculator()

        masses = [float(d['mass']) for d in data if 'XXmassXX' in d]

        return calculator.avg(masses)

    def xǁMeteoriteStatsǁaverage_mass__mutmut_7(self, data):
        calculator = SimpleCalculator()

        masses = [float(d['mass']) for d in data if 'MASS' in d]

        return calculator.avg(masses)

    def xǁMeteoriteStatsǁaverage_mass__mutmut_8(self, data):
        calculator = SimpleCalculator()

        masses = [float(d['mass']) for d in data if 'mass' not in d]

        return calculator.avg(masses)

    def xǁMeteoriteStatsǁaverage_mass__mutmut_9(self, data):
        calculator = SimpleCalculator()

        masses = [float(d['mass']) for d in data if 'mass' in d]

        return calculator.avg(None)
    
    xǁMeteoriteStatsǁaverage_mass__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁMeteoriteStatsǁaverage_mass__mutmut_1': xǁMeteoriteStatsǁaverage_mass__mutmut_1, 
        'xǁMeteoriteStatsǁaverage_mass__mutmut_2': xǁMeteoriteStatsǁaverage_mass__mutmut_2, 
        'xǁMeteoriteStatsǁaverage_mass__mutmut_3': xǁMeteoriteStatsǁaverage_mass__mutmut_3, 
        'xǁMeteoriteStatsǁaverage_mass__mutmut_4': xǁMeteoriteStatsǁaverage_mass__mutmut_4, 
        'xǁMeteoriteStatsǁaverage_mass__mutmut_5': xǁMeteoriteStatsǁaverage_mass__mutmut_5, 
        'xǁMeteoriteStatsǁaverage_mass__mutmut_6': xǁMeteoriteStatsǁaverage_mass__mutmut_6, 
        'xǁMeteoriteStatsǁaverage_mass__mutmut_7': xǁMeteoriteStatsǁaverage_mass__mutmut_7, 
        'xǁMeteoriteStatsǁaverage_mass__mutmut_8': xǁMeteoriteStatsǁaverage_mass__mutmut_8, 
        'xǁMeteoriteStatsǁaverage_mass__mutmut_9': xǁMeteoriteStatsǁaverage_mass__mutmut_9
    }
    
    def average_mass(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMeteoriteStatsǁaverage_mass__mutmut_orig"), object.__getattribute__(self, "xǁMeteoriteStatsǁaverage_mass__mutmut_mutants"), args, kwargs, self)
        return result 
    
    average_mass.__signature__ = _mutmut_signature(xǁMeteoriteStatsǁaverage_mass__mutmut_orig)
    xǁMeteoriteStatsǁaverage_mass__mutmut_orig.__name__ = 'xǁMeteoriteStatsǁaverage_mass'
