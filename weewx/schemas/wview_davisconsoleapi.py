#
#    Copyright (c) 2009-2020 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your rights.
#
"""The extended wview schema."""

# =============================================================================
# This is a list containing the default schema of the archive database.  It is
# only used for initialization --- afterwards, the schema is obtained
# dynamically from the database.  Although a type may be listed here, it may
# not necessarily be supported by your weather station hardware.
# =============================================================================
# NB: This schema is specified using the WeeWX V4 "new-style" schema.
# =============================================================================
table = [('dateTime',             'INTEGER NOT NULL UNIQUE PRIMARY KEY'),
    ('usUnits',              'INTEGER NOT NULL'),
    ('interval',             'INTEGER NOT NULL'),
    ("altimeter", "REAL"),
    ("appTemp", "REAL"),
    ("appTemp1", "REAL"),
    ("appUptimeC", "INTEGER"),
    ("barometer", "REAL"),
    ("batteryConditionC", "INTEGER"),
    ("batteryCurrentC", "REAL"),
    ("batteryCycleCountC", "INTEGER"),
    ("batteryPercentC", "INTEGER"),
    ("batteryStatus1", "REAL"),
    ("batteryStatus2", "REAL"),
    ("batteryStatus3", "REAL"),
    ("batteryStatus4", "REAL"),
    ("batteryStatus5", "REAL"),
    ("batteryStatus6", "REAL"),
    ("batteryStatus7", "REAL"),
    ("batteryStatus8", "REAL"),
    ("batteryStatusC", "INTEGER"),
    ("batteryTempC", "INTEGER"),
    ("bootloaderVersionC", "INTEGER"),
    ("chargerPluggedC", "INTEGER"),
    ("clockSourceC", "INTEGER"),
    ("cloudbase", "REAL"),
    ("co", "REAL"),
    ("co2", "REAL"),
    ("co2_Batt", "REAL"),
    ("co2_Hum", "REAL"),
    ("co2_Temp", "REAL"),
    ("connectionUptimeC", "INTEGER"),
    ("consBatteryVoltage", "REAL"),
    ("consoleApiLevelC", "INTEGER"),
    ("consoleBatteryC", "REAL"),
    ("consoleOsVersionC", "TEXT"),
    ("consoleRadioVersionC", "TEXT"),
    ("consoleSwVersionC", "TEXT"),
    ("databaseKilobytesC", "INTEGER"),
    ("dewpoint", "REAL"),
    ("dewpoint1", "REAL"),
    ("dewpoint2", "REAL"),
    ("ET", "REAL"),
    ("ET_2", "REAL"),
    ("extraHumid1", "REAL"),
    ("extraHumid2", "REAL"),
    ("extraHumid3", "REAL"),
    ("extraHumid4", "REAL"),
    ("extraHumid5", "REAL"),
    ("extraHumid6", "REAL"),
    ("extraHumid7", "REAL"),
    ("extraHumid8", "REAL"),
    ("extraTemp1", "REAL"),
    ("extraTemp2", "REAL"),
    ("extraTemp3", "REAL"),
    ("extraTemp4", "REAL"),
    ("extraTemp5", "REAL"),
    ("extraTemp6", "REAL"),
    ("extraTemp7", "REAL"),
    ("extraTemp8", "REAL"),
    ("forecast", "REAL"),
    ("freeMemC", "INTEGER"),
    ("healthVersionC", "INTEGER"),
    ("heatindex", "REAL"),
    ("heatindex1", "REAL"),
    ("heatindex2", "REAL"),
    ("humidex", "REAL"),
    ("humidex1", "REAL"),
    ("iFreeSpaceC", "INTEGER"),
    ("inDewpoint", "REAL"),
    ("inHumidity", "REAL"),
    ("inTemp", "REAL"),
    ("inTempBatteryStatus", "REAL"),
    ("leafTemp1", "REAL"),
    ("leafTemp2", "REAL"),
    ("leafWet1", "REAL"),
    ("leafWet2", "REAL"),
    ("linkUptimeC", "INTEGER"),
    ("localAPIQueriesC", "INTEGER"),
    ("luminosity", "REAL"),
    ("maxSolarRad", "REAL"),
    ("osUptimeC", "INTEGER"),
    ("outHumidity", "REAL"),
    ("outHumidity_2", "REAL"),
    ("outTemp", "REAL"),
    ("outTempBatteryStatus", "REAL"),
    ("outTemp_2", "REAL"),
    ("outWetbulb", "REAL"),
    ("outWetbulb_2", "REAL"),
    ("pm10_0", "REAL"),
    ("pm1_0", "REAL"),
    ("pm2_5", "REAL"),
    ("pressure", "REAL"),
    ("queueKilobytesC", "INTEGER"),
    ("radiation", "REAL"),
    ("radiation_2", "REAL"),
    ("rain", "REAL"),
    ("rainBatteryStatus", "REAL"),
    ("rainBatteryStatus_2", "REAL"),
    ("rainDur", "REAL"),
    ("rainDur_2", "REAL"),
    ("rainRate", "REAL"),
    ("rainRate_2", "REAL"),
    ("rain_2", "REAL"),
    ("rssi", "REAL"),
    ("rssi2", "REAL"),
    ("rssi3", "REAL"),
    ("rssi4", "REAL"),
    ("rssi5", "REAL"),
    ("rssi6", "REAL"),
    ("rssi7", "REAL"),
    ("rssi8", "REAL"),
    ("rssiA", "REAL"),
    ("rssiC", "REAL"),
    ("rssir", "REAL"),
    ("rssiw", "REAL"),
    ("rssi_2", "REAL"),
    ("rxCheckPercent", "REAL"),
    ("rxCheckPercent2", "REAL"),
    ("rxCheckPercent3", "REAL"),
    ("rxCheckPercent4", "REAL"),
    ("rxCheckPercent5", "REAL"),
    ("rxCheckPercent6", "REAL"),
    ("rxCheckPercent7", "REAL"),
    ("rxCheckPercent8", "REAL"),
    ("rxCheckPercenta", "REAL"),
    ("rxCheckPercentr", "REAL"),
    ("rxCheckPercentw", "REAL"),
    ("rxCheckPercent_2", "REAL"),
    ("rxKilobytesC", "INTEGER"),
    ("signal1", "REAL"),
    ("signal2", "REAL"),
    ("signal3", "REAL"),
    ("signal4", "REAL"),
    ("signal5", "REAL"),
    ("signal6", "REAL"),
    ("signal7", "REAL"),
    ("signal8", "REAL"),
    ("signala", "REAL"),
    ("signalr", "REAL"),
    ("signalw", "REAL"),
    ("signal_2", "REAL"),
    ("soilMoist1", "REAL"),
    ("soilMoist2", "REAL"),
    ("soilMoist3", "REAL"),
    ("soilMoist4", "REAL"),
    ("soilTemp1", "REAL"),
    ("soilTemp2", "REAL"),
    ("soilTemp3", "REAL"),
    ("soilTemp4", "REAL"),
    ("solarVolt", "REAL"),
    ("solarVolt_2", "REAL"),
    ("sunshineDur", "REAL"),
    ("sunshineDur_2", "REAL"),
    ("sunshine_hours", "REAL"),
    ("sunshine_time", "REAL"),
    ("supercapVolt", "REAL"),
    ("supercapVolt_2", "REAL"),
    ("supplyVoltage", "REAL"),
    ("systemFreeSpaceC", "INTEGER"),
    ("THSW", "REAL"),
    ("THSW_2", "REAL"),
    ("THW", "REAL"),
    ("THW_2", "REAL"),
    ("txBatteryStatus", "REAL"),
    ("txBatteryStatus_2", "REAL"),
    ("txBatteryVolt", "REAL"),
    ("txBatteryVolt_2", "REAL"),
    ("txID", "INTEGER"),
    ("txID2", "INTEGER"),
    ("txID3", "INTEGER"),
    ("txID4", "INTEGER"),
    ("txID5", "INTEGER"),
    ("txID6", "INTEGER"),
    ("txID7", "INTEGER"),
    ("txID8", "INTEGER"),
    ("txIDr", "INTEGER"),
    ("txIDw", "INTEGER"),
    ("txID_2", "INTEGER"),
    ("txKilobytesC", "INTEGER"),
    ("UV", "REAL"),
    ("uvBatteryStatus", "REAL"),
    ("UV_2", "REAL"),
    ("windBatteryStatus", "REAL"),
    ("windchill", "REAL"),
    ("windchill2", "REAL"),
    ("windDir", "REAL"),
    ("windDir_2", "REAL"),
    ("windGust", "REAL"),
    ("windGustSpeed10", "REAL"),
    ("windGustDir", "REAL"),
    ("windGustDir_2", "REAL"),
    ("windGust_2", "REAL"),
    ("windGustSpeed10_2", "REAL"),
    ("windrun", "REAL"),
    ("windrun_2", "REAL"),
    ("windSpeed", "REAL"),
    ("windSpeed_2", "REAL"),
    ]

day_summaries = [(e[0], 'scalar') for e in table
                 if e[0] not in ('dateTime', 'usUnits', 'interval', 'consoleOsVersionC', 'consoleRadioVersionC' ,'consoleSwVersionC')] + [('wind', 'VECTOR')]

schema = {
    'table': table,
    'day_summaries' : day_summaries
}
