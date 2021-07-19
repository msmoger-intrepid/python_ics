# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class nameless889(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('id_29_bit_enable', ctypes.c_uint, 1),
        ('fc_id_29_bit_enable', ctypes.c_uint, 1),
        ('ext_address_enable', ctypes.c_uint, 1),
        ('fc_ext_address_enable', ctypes.c_uint, 1),
        ('enableFlowControlTransmission', ctypes.c_uint, 1),
        ('paddingEnable', ctypes.c_uint, 1),
        ('iscanFD', ctypes.c_uint, 1),
        ('isBRSEnabled', ctypes.c_uint, 1),
    ]



class nameless29209(ctypes.Union):
    _pack_ = 2
    _anonymous_  = ('nameless889',)
    _fields_ = [
        ('nameless889', nameless889),
        ('flags', ctypes.c_uint32),
    ]



class st_cm_iso157652_rx_message(ctypes.Structure):
    _pack_ = 2
    _anonymous_  = ('nameless29209',)
    _fields_ = [
        ('vs_netid', ctypes.c_uint16),
        ('padding', ctypes.c_uint8),
        ('id', ctypes.c_uint32),
        ('id_mask', ctypes.c_uint32),
        ('fc_id', ctypes.c_uint32),
        ('flowControlExtendedAddress', ctypes.c_uint8),
        ('extendedAddress', ctypes.c_uint8),
        ('blockSize', ctypes.c_uint8),
        ('stMin', ctypes.c_uint8),
        ('cf_timeout', ctypes.c_uint16),
        ('nameless29209', nameless29209),
        ('reserved', ctypes.c_uint8 * 16),
    ]


_stCM_ISO157652_RxMessage = st_cm_iso157652_rx_message
stCM_ISO157652_RxMessage = st_cm_iso157652_rx_message

