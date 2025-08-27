# -*- coding: utf-8 -*-

import operator
from functools import reduce
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


class SimpleCalculator:
    def xǁSimpleCalculatorǁadd__mutmut_orig(self, *args):
        return sum(args)
    def xǁSimpleCalculatorǁadd__mutmut_1(self, *args):
        return sum(None)
    
    xǁSimpleCalculatorǁadd__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSimpleCalculatorǁadd__mutmut_1': xǁSimpleCalculatorǁadd__mutmut_1
    }
    
    def add(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSimpleCalculatorǁadd__mutmut_orig"), object.__getattribute__(self, "xǁSimpleCalculatorǁadd__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add.__signature__ = _mutmut_signature(xǁSimpleCalculatorǁadd__mutmut_orig)
    xǁSimpleCalculatorǁadd__mutmut_orig.__name__ = 'xǁSimpleCalculatorǁadd'

    def xǁSimpleCalculatorǁsub__mutmut_orig(self, a, b):
        return a - b

    def xǁSimpleCalculatorǁsub__mutmut_1(self, a, b):
        return a + b
    
    xǁSimpleCalculatorǁsub__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSimpleCalculatorǁsub__mutmut_1': xǁSimpleCalculatorǁsub__mutmut_1
    }
    
    def sub(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSimpleCalculatorǁsub__mutmut_orig"), object.__getattribute__(self, "xǁSimpleCalculatorǁsub__mutmut_mutants"), args, kwargs, self)
        return result 
    
    sub.__signature__ = _mutmut_signature(xǁSimpleCalculatorǁsub__mutmut_orig)
    xǁSimpleCalculatorǁsub__mutmut_orig.__name__ = 'xǁSimpleCalculatorǁsub'

    def xǁSimpleCalculatorǁmul__mutmut_orig(self, *args):
        if not all(args):
            raise ValueError
        return reduce(operator.mul, args)

    def xǁSimpleCalculatorǁmul__mutmut_1(self, *args):
        if all(args):
            raise ValueError
        return reduce(operator.mul, args)

    def xǁSimpleCalculatorǁmul__mutmut_2(self, *args):
        if not all(None):
            raise ValueError
        return reduce(operator.mul, args)

    def xǁSimpleCalculatorǁmul__mutmut_3(self, *args):
        if not all(args):
            raise ValueError
        return reduce(None, args)

    def xǁSimpleCalculatorǁmul__mutmut_4(self, *args):
        if not all(args):
            raise ValueError
        return reduce(operator.mul, None)

    def xǁSimpleCalculatorǁmul__mutmut_5(self, *args):
        if not all(args):
            raise ValueError
        return reduce(args)

    def xǁSimpleCalculatorǁmul__mutmut_6(self, *args):
        if not all(args):
            raise ValueError
        return reduce(operator.mul, )
    
    xǁSimpleCalculatorǁmul__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSimpleCalculatorǁmul__mutmut_1': xǁSimpleCalculatorǁmul__mutmut_1, 
        'xǁSimpleCalculatorǁmul__mutmut_2': xǁSimpleCalculatorǁmul__mutmut_2, 
        'xǁSimpleCalculatorǁmul__mutmut_3': xǁSimpleCalculatorǁmul__mutmut_3, 
        'xǁSimpleCalculatorǁmul__mutmut_4': xǁSimpleCalculatorǁmul__mutmut_4, 
        'xǁSimpleCalculatorǁmul__mutmut_5': xǁSimpleCalculatorǁmul__mutmut_5, 
        'xǁSimpleCalculatorǁmul__mutmut_6': xǁSimpleCalculatorǁmul__mutmut_6
    }
    
    def mul(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSimpleCalculatorǁmul__mutmut_orig"), object.__getattribute__(self, "xǁSimpleCalculatorǁmul__mutmut_mutants"), args, kwargs, self)
        return result 
    
    mul.__signature__ = _mutmut_signature(xǁSimpleCalculatorǁmul__mutmut_orig)
    xǁSimpleCalculatorǁmul__mutmut_orig.__name__ = 'xǁSimpleCalculatorǁmul'

    def xǁSimpleCalculatorǁdiv__mutmut_orig(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float("inf")

    def xǁSimpleCalculatorǁdiv__mutmut_1(self, a, b):
        try:
            return a * b
        except ZeroDivisionError:
            return float("inf")

    def xǁSimpleCalculatorǁdiv__mutmut_2(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float(None)

    def xǁSimpleCalculatorǁdiv__mutmut_3(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float("XXinfXX")

    def xǁSimpleCalculatorǁdiv__mutmut_4(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float("INF")
    
    xǁSimpleCalculatorǁdiv__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSimpleCalculatorǁdiv__mutmut_1': xǁSimpleCalculatorǁdiv__mutmut_1, 
        'xǁSimpleCalculatorǁdiv__mutmut_2': xǁSimpleCalculatorǁdiv__mutmut_2, 
        'xǁSimpleCalculatorǁdiv__mutmut_3': xǁSimpleCalculatorǁdiv__mutmut_3, 
        'xǁSimpleCalculatorǁdiv__mutmut_4': xǁSimpleCalculatorǁdiv__mutmut_4
    }
    
    def div(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSimpleCalculatorǁdiv__mutmut_orig"), object.__getattribute__(self, "xǁSimpleCalculatorǁdiv__mutmut_mutants"), args, kwargs, self)
        return result 
    
    div.__signature__ = _mutmut_signature(xǁSimpleCalculatorǁdiv__mutmut_orig)
    xǁSimpleCalculatorǁdiv__mutmut_orig.__name__ = 'xǁSimpleCalculatorǁdiv'

    def xǁSimpleCalculatorǁavg__mutmut_orig(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_1(self, it, lt=None, ut=None):
        count = None
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_2(self, it, lt=None, ut=None):
        count = 1
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_3(self, it, lt=None, ut=None):
        count = 0
        total = None

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_4(self, it, lt=None, ut=None):
        count = 0
        total = 1

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_5(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None or number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_6(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_7(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number <= lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_8(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                break
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_9(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None or number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_10(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_11(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number >= ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_12(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                break
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_13(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count = 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_14(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count -= 1
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_15(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 2
            total += number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_16(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total = number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_17(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total -= number

        if count == 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_18(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count != 0:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_19(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 1:
            return 0

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_20(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 1

        return total / count

    def xǁSimpleCalculatorǁavg__mutmut_21(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total * count
    
    xǁSimpleCalculatorǁavg__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSimpleCalculatorǁavg__mutmut_1': xǁSimpleCalculatorǁavg__mutmut_1, 
        'xǁSimpleCalculatorǁavg__mutmut_2': xǁSimpleCalculatorǁavg__mutmut_2, 
        'xǁSimpleCalculatorǁavg__mutmut_3': xǁSimpleCalculatorǁavg__mutmut_3, 
        'xǁSimpleCalculatorǁavg__mutmut_4': xǁSimpleCalculatorǁavg__mutmut_4, 
        'xǁSimpleCalculatorǁavg__mutmut_5': xǁSimpleCalculatorǁavg__mutmut_5, 
        'xǁSimpleCalculatorǁavg__mutmut_6': xǁSimpleCalculatorǁavg__mutmut_6, 
        'xǁSimpleCalculatorǁavg__mutmut_7': xǁSimpleCalculatorǁavg__mutmut_7, 
        'xǁSimpleCalculatorǁavg__mutmut_8': xǁSimpleCalculatorǁavg__mutmut_8, 
        'xǁSimpleCalculatorǁavg__mutmut_9': xǁSimpleCalculatorǁavg__mutmut_9, 
        'xǁSimpleCalculatorǁavg__mutmut_10': xǁSimpleCalculatorǁavg__mutmut_10, 
        'xǁSimpleCalculatorǁavg__mutmut_11': xǁSimpleCalculatorǁavg__mutmut_11, 
        'xǁSimpleCalculatorǁavg__mutmut_12': xǁSimpleCalculatorǁavg__mutmut_12, 
        'xǁSimpleCalculatorǁavg__mutmut_13': xǁSimpleCalculatorǁavg__mutmut_13, 
        'xǁSimpleCalculatorǁavg__mutmut_14': xǁSimpleCalculatorǁavg__mutmut_14, 
        'xǁSimpleCalculatorǁavg__mutmut_15': xǁSimpleCalculatorǁavg__mutmut_15, 
        'xǁSimpleCalculatorǁavg__mutmut_16': xǁSimpleCalculatorǁavg__mutmut_16, 
        'xǁSimpleCalculatorǁavg__mutmut_17': xǁSimpleCalculatorǁavg__mutmut_17, 
        'xǁSimpleCalculatorǁavg__mutmut_18': xǁSimpleCalculatorǁavg__mutmut_18, 
        'xǁSimpleCalculatorǁavg__mutmut_19': xǁSimpleCalculatorǁavg__mutmut_19, 
        'xǁSimpleCalculatorǁavg__mutmut_20': xǁSimpleCalculatorǁavg__mutmut_20, 
        'xǁSimpleCalculatorǁavg__mutmut_21': xǁSimpleCalculatorǁavg__mutmut_21
    }
    
    def avg(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSimpleCalculatorǁavg__mutmut_orig"), object.__getattribute__(self, "xǁSimpleCalculatorǁavg__mutmut_mutants"), args, kwargs, self)
        return result 
    
    avg.__signature__ = _mutmut_signature(xǁSimpleCalculatorǁavg__mutmut_orig)
    xǁSimpleCalculatorǁavg__mutmut_orig.__name__ = 'xǁSimpleCalculatorǁavg'
