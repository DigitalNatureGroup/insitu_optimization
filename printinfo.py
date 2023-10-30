# printinfo.py
#
# This file is part of the LibTiePie programming examples.
#
# Find more information on http://www.tiepie.com/LibTiePie .

from __future__ import print_function
from libtiepie import *
from libtiepie.exceptions import LibTiePieException
from libtiepie.device import Device
from libtiepie.oscilloscope import Oscilloscope
from libtiepie.generator import Generator
from libtiepie.i2chost import I2CHost
from libtiepie.server import Server


def print_library_info():
    print('Library:')
    print('  Version      : ' + str(library.version) + library.version_extra)
    print('  Configuration: ' + library.config_str)


def print_device_info(dev, full=True):
    if not isinstance(dev, Device):
        raise

    print('Device:')
    print('  Name                      : ' + dev.name)
    print('  Short name                : ' + dev.name_short)
    print('  Serial number             : ' + str(dev.serial_number))
    try:
        print('  Calibration date          : {0:%Y-%m-%d}'.format(dev.calibration_date))
    except LibTiePieException:
        pass
    print('  Product id                : ' + str(dev.product_id))
    print('  Vendor id                 : ' + str(dev.vendor_id))
    try:
        print('  Driver version            : ' + str(dev.driver_version))
    except LibTiePieException:
        pass
    try:
        print('  Firmware version          : ' + str(dev.firmware_version))
    except LibTiePieException:
        pass
    try:
        print('  IPv4 address              : ' + ipv4_str(dev.ipv4_address))
    except LibTiePieException:
        pass
    try:
        print('  IP port                   : ' + str(dev.ip_port))
    except LibTiePieException:
        pass

    print('  Has battery               : ' + str(dev.has_battery))
    if dev.has_battery:
        print('  Battery:')
        try:
            print('    Charge                  : ' + str(dev.battery_charge) + ' %')
        except LibTiePieException:
            pass
        try:
            print('    Time to empty           : ' + str(dev.battery_time_to_empty) + ' minutes')
        except LibTiePieException:
            pass
        try:
            print('    Time to full            : ' + str(dev.battery_time_to_full) + ' minutes')
        except LibTiePieException:
            pass
        try:
            print('    Charger connected       : ' + str(dev.is_battery_charger_connected))
        except LibTiePieException:
            pass
        try:
            print('    Charging                : ' + str(dev.is_battery_charging))
        except LibTiePieException:
            pass
        try:
            print('    Broken                  : ' + str(dev.is_battery_broken))
        except LibTiePieException:
            pass

    if full:
        if isinstance(dev, Oscilloscope):
            print_oscilloscope_info(dev)
        elif isinstance(dev, Generator):
            print_generator_info(dev)
        elif isinstance(dev, I2CHost):
            print_i2c_info(dev)


def print_oscilloscope_info(scp):
    if not isinstance(scp, Oscilloscope):
        raise

    print('Oscilloscope:')
    print('  Channel count             : ' + str(len(scp.channels)))
    print('  Connection test           : ' + str(scp.has_connection_test))
    print('  Measure modes             : ' + measure_mode_str(scp.measure_modes))
    print('  Measure mode              : ' + measure_mode_str(scp.measure_mode))
    print('  Auto resolution modes     : ' + auto_resolution_mode_str(scp.auto_resolution_modes))
    print('  Auto resolution mode      : ' + auto_resolution_mode_str(scp.auto_resolution_mode))
    print('  Resolutions               : ' + ', '.join(map(str, scp.resolutions)))
    print('  Resolution                : ' + str(scp.resolution))
    print('  Resolution enhanced       : ' + str(scp.is_resolution_enhanced))
    print('  Clock outputs             : ' + clock_output_str(scp.clock_outputs))
    print('  Clock output              : ' + clock_output_str(scp.clock_output))
    try:
        print('  Clock output frequecies   : ' + ', '.join(map(str, scp.clock_output_frequencies)))
        print('  Clock output frequency    : ' + str(scp.clock_output_frequency))
    except LibTiePieException:
        pass
    print('  Clock sources             : ' + clock_source_str(scp.clock_sources))
    print('  Clock source              : ' + clock_source_str(scp.clock_source))
    try:
        print('  Clock source frequecies   : ' + ', '.join(map(str, scp.clock_source_frequencies)))
        print('  Clock source frequency    : ' + str(scp.clock_source_frequency))
    except LibTiePieException:
        pass

    print('  Record length max         : ' + str(scp.record_length_max))
    print('  Record length             : ' + str(scp.record_length))
    print('  Sample frequency max      : ' + str(scp.sample_frequency_max))
    print('  Sample frequency          : ' + str(scp.sample_frequency))

    if scp.measure_mode == MM_BLOCK:
        print('  Segment count max         : ' + str(scp.segment_count_max))
        if scp.segment_count_max > 1:
            print('  Segment count             : ' + str(scp.segment_count))

    if scp.has_trigger:
        print('  Pre sample ratio          : ' + str(scp.pre_sample_ratio))
        to = scp.trigger_time_out
        if to == TO_INFINITY:
            to = 'Infinite'
        print('  Trigger time out          : ' + str(to))
        if scp.has_trigger_delay:
            print('  Trigger delay max         : ' + str(scp.trigger_delay_max))
            print('  Trigger delay             : ' + str(scp.trigger_delay))
        if scp.has_trigger_hold_off:
            print('  Trigger holf off count max: ' + str(scp.trigger_hold_off_count_max))
            print('  Trigger holf off count    : ' + str(scp.trigger_hold_off_count))

    if len(scp.channels) > 0:
        num = 1
        for ch in scp.channels:
            print('  Channel {:d}:'.format(num))
            print('    Connector type          : ' + connector_type_str(ch.connector_type))
            print('    Differential            : ' + str(ch.is_differential))
            print('    Impedance               : ' + str(ch.impedance))
            print('    Connection test         : ' + str(ch.has_connection_test))
            print('    Available               : ' + str(ch.is_available))
            print('    Enabled                 : ' + str(ch.enabled))
            print('    Bandwidths              : ' + ', '.join(map(str, ch.bandwidths)))
            print('    Bandwidth               : ' + str(ch.bandwidth))
            print('    Couplings               : ' + coupling_str(ch.couplings))
            print('    Coupling                : ' + coupling_str(ch.coupling))
            print('    Auto ranging            : ' + str(ch.auto_ranging))
            print('    Ranges                  : ' + ', '.join(map(str, ch.ranges)))
            print('    Range                   : ' + str(ch.range))
            print('    Probe gain              : ' + str(ch.probe_gain))
            print('    Probe offset            : ' + str(ch.probe_offset))
            if ch.has_trigger:
                tr = ch.trigger
                print('    Trigger:')
                print('      Available             : ' + str(tr.is_available))
                print('      Enabled               : ' + str(tr.enabled))
                print('      Kinds                 : ' + trigger_kind_str(tr.kinds))
                print('      Kind                  : ' + trigger_kind_str(tr.kind))
                print('      Level modes           : ' + trigger_level_mode_str(tr.level_modes))
                print('      Level mode            : ' + trigger_level_mode_str(tr.level_mode))
                print('      Levels                : ' + ', '.join(map(str, tr.levels)))
                print('      Hystereses            : ' + ', '.join(map(str, tr.hystereses)))
                print('      Conditions            : ' + trigger_condition_str(tr.conditions))
                if tr.conditions != TCM_NONE:
                    print('      Condition             : ' + trigger_condition_str(tr.condition))
                print('      Times                 : ' + ', '.join(map(str, tr.times)))
            num += 1

    print_trigger_inputs_info(scp)
    print_trigger_outputs_info(scp)


def print_generator_info(gen):
    if not isinstance(gen, Generator):
        raise

    print('Generator:')
    print('  Connector type            : ' + connector_type_str(gen.connector_type))
    print('  Differential              : ' + str(gen.is_differential))
    print('  Controllable              : ' + str(gen.is_controllable))
    print('  Impedance                 : ' + str(gen.impedance))
    print('  Resolution                : ' + str(gen.resolution))
    print('  Output value min          : ' + str(gen.output_value_min))
    print('  Output value max          : ' + str(gen.output_value_max))
    print('  Output on                 : ' + str(gen.output_on))
    if gen.has_output_invert:
        print('  Output invert             : ' + str(gen.output_invert))

    print('  Modes native              : ' + generator_mode_str(gen.modes_native))
    print('  Modes                     : ' + generator_mode_str(gen.modes))
    if gen.modes != GMM_NONE:
        print('  Mode                      : ' + generator_mode_str(gen.mode))
        if (gen.mode & GMM_BURST_COUNT) != 0:
            print('  Burst active              : ' + str(gen.is_burst_active))
            print('  Burst count max           : ' + str(gen.burst_count_max))
            print('  Burst count               : ' + str(gen.burst_count))
        if (gen.mode & GMM_BURST_SAMPLE_COUNT) != 0:
            print('  Burst sample count max    : ' + str(gen.burst_sample_count_max))
            print('  Burst sample count        : ' + str(gen.burst_sample_count))
        if (gen.mode & GMM_BURST_SEGMENT_COUNT) != 0:
            print('  Burst segment count max   : ' + str(gen.burst_segment_count_max))
            print('  Burst segment count       : ' + str(gen.burst_segment_count))

    print('  Signal types              : ' + signal_type_str(gen.signal_types))
    print('  Signal type               : ' + signal_type_str(gen.signal_type))

    if gen.has_amplitude:
        print('  Amplitude min             : ' + str(gen.amplitude_min))
        print('  Amplitude max             : ' + str(gen.amplitude_max))
        print('  Amplitude                 : ' + str(gen.amplitude))
        print('  Amplitude ranges          : ' + ', '.join(map(str, gen.amplitude_ranges)))
        print('  Amplitude range           : ' + str(gen.amplitude_range))
        print('  Amplitude auto ranging    : ' + str(gen.amplitude_auto_ranging))

    if gen.has_frequency:
        print('  Frequency modes           : ' + frequency_mode_str(gen.frequency_modes))
        print('  Frequency mode            : ' + frequency_mode_str(gen.frequency_mode))
        print('  Frequency min             : ' + str(gen.frequency_min))
        print('  Frequency max             : ' + str(gen.frequency_max))
        print('  Frequency                 : ' + str(gen.frequency))

    if gen.has_offset:
        print('  Offset min                : ' + str(gen.offset_min))
        print('  Offset max                : ' + str(gen.offset_max))
        print('  Offset                    : ' + str(gen.offset))

    if gen.has_phase:
        print('  Phase min                 : ' + str(gen.phase_min))
        print('  Phase max                 : ' + str(gen.phase_max))
        print('  Phase                     : ' + str(gen.phase))

    if gen.has_symmetry:
        print('  Symmetry min              : ' + str(gen.symmetry_min))
        print('  Symmetry max              : ' + str(gen.symmetry_max))
        print('  Symmetry                  : ' + str(gen.symmetry))

    if gen.has_width:
        print('  Width min                 : ' + str(gen.width_min))
        print('  Width max                 : ' + str(gen.width_max))
        print('  Width                     : ' + str(gen.width))

    if gen.has_edge_time:
        print('  Leading edge time min     : ' + str(gen.leading_edge_time_min))
        print('  Leading edge time max     : ' + str(gen.leading_edge_time_max))
        print('  Leading edge time         : ' + str(gen.leading_edge_time))
        print('  Trailing edge time min    : ' + str(gen.trailing_edge_time_min))
        print('  Trailing edge time max    : ' + str(gen.trailing_edge_time_max))
        print('  Trailing edge time        : ' + str(gen.trailing_edge_time))

    if gen.has_data:
        print('  Data length min           : ' + str(gen.data_length_min))
        print('  Data length max           : ' + str(gen.data_length_max))
        print('  Data length               : ' + str(gen.data_length))

    print_trigger_inputs_info(gen)
    print_trigger_outputs_info(gen)


def print_i2c_info(i2c):
    if not isinstance(i2c, I2CHost):
        raise

    print('I2C Host:')
    print('  Internal addresses        : ' + ', '.join(map(str, i2c.internal_addresses)))
    print('  Speed max                 : ' + str(i2c.speed_max))
    print('  Speed                     : ' + str(i2c.speed))

    print_trigger_inputs_info(i2c)
    print_trigger_outputs_info(i2c)


def print_trigger_inputs_info(dev):
    if not isinstance(dev, Device):
        raise

    if len(dev.trigger_inputs) > 0:
        num = 1
        for trin in dev.trigger_inputs:
            print('  Trigger input {:d}:'.format(num))
            print('    Id                      : ' + str(trin.id))
            print('    Name                    : ' + str(trin.name))
            print('    Available               : ' + str(trin.is_available))
            if trin.is_available:
                print('    Enabled                 : ' + str(trin.enabled))
                print('    Kinds                   : ' + trigger_kind_str(trin.kinds))
                if trin.kinds != TKM_NONE:
                    print('    Kind                    : ' + trigger_kind_str(trin.kind))
            num += 1


def print_trigger_outputs_info(dev):
    if not isinstance(dev, Device):
        raise

    if len(dev.trigger_outputs) > 0:
        num = 1
        for trout in dev.trigger_outputs:
            print('  Trigger output {:d}:'.format(num))
            print('    Id                      : ' + str(trout.id))
            print('    Name                    : ' + str(trout.name))
            print('    Enabled                 : ' + str(trout.enabled))
            print('    Events                  : ' + trigger_output_event_str(trout.events))
            print('    Event                   : ' + trigger_output_event_str(trout.event))
            num += 1


def print_server_info(srv):
    if not isinstance(srv, Server):
        raise

    print('Server:')
    print('  URL                       : ' + srv.url)
    print('  Name                      : ' + srv.name)
    print('  Description               : ' + srv.description)
    print('  IPv4 address              : ' + ipv4_str(srv.ipv4_address))
    print('  IP port                   : ' + str(srv.ip_port))
    print('  Id                        : ' + srv.id)
    print('  Version                   : ' + str(srv.version) + srv.version_extra)
    print('  Status                    : ' + server_status_str(srv.status))
    if srv.last_error != SERVER_ERROR_NONE:
        print('  Last error                : ' + server_error_str(srv.last_error))
