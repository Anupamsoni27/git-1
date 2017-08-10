import csv


a1 = ""
a2 = ""
a3 = ""
a4 = ""
f = open('LIST3.csv')
rows = csv.reader(f)

for row in rows:
 r=list(row)
 for r in row:
  s1_row = row[0]
  if "Northeast Asia" in s1_row:
     a2 = "NEAS"
  elif "China" in s1_row:
     a2 = "CH"
  elif "Japan" in s1_row:
     a2 = "JP"
  elif "Korea" in s1_row:
     a2 = "KR"
  elif "Taiwan" in s1_row:
     a2 = "TW"

  if "LDPE" in s1_row:
       a1 = "LDPE"
  elif "EPS" in s1_row:
     a2 = "EPS"
  elif "PET" in s1_row:
     a2 = "PET"
  elif "HDPE" in s1_row:
     a2 = "HDPE"
  elif "LLDPE" in s1_row:
      a2 = "LLDPE"
  elif "PP" in s1_row:
      a2 = "PP"
  elif "Polystyrene" in s1_row:
      a2 = "PS"
  else: pass

  s3_row = r
  if "Nameplate" in s3_row:
       a4 = "NPC"
  elif "Nameplate" in s3_row:
       a4 = "NPC"
  elif "Operating Rate (%)" in s3_row:
       a4 = "OPRT"
  elif "Production" in s3_row:
       a4 = "PRD"
  elif "Imports" in s3_row:
       a4 = "IMP"
  elif "Total Supply" in s3_row:
       a4 = "TSP"
  elif "Film & Sheet" in s3_row:
       a4 = "FS"
  elif "Injection Molding" in s3_row:
       a4 = "INJM"
  elif "Pipe & Extrusion" in s3_row:
       a4 = "PE"
  elif "Extrusion Coating" in s3_row:
       a4 = "EC"
  elif "Blow Molding" in s3_row:
       a4 = "BM"
  elif "Wire & Cable" in s3_row:
       a4 = "WC"
  elif "Other" in s3_row:
       a4 = "OTHER"
  elif "Domestic Demand" in s3_row:
       a4 = "DD"
  elif "Exports" in s3_row:
       a4 = "EXP"
  elif "Total Demand" in s3_row:
       a4 = "TTLDEM"
  elif "Inventory Change" in s3_row:
       a4 = "INVCNG"
  elif "Rotomolding" in s3_row:
       a4 = "RM"
  elif "Fiber" in s3_row:
       a4 = "FIBER"
  elif "Raffia" in s3_row:
       a4 = "RAFFIA"
  elif "Nameplate Capacity" in s3_row:
       a4 = "NPC"
  elif "Total Production" in s3_row:
       a4 = "PRD"
  elif "Packaging" in s3_row:
       a4 = "PCKG"
  elif "Consumer Products" in s3_row:
       a4 = "CP"
  elif "Electronics / Appliances" in s3_row:
       a4 = "EA"
  elif "Building / Construction" in s3_row:
       a4 = "BC"
  elif "Others" in s3_row:
       a4 = "PS"
  elif "Homo/Copolymers" in s3_row:
       a4 = "HC"
  elif "Dispersion/Emulsion" in s3_row:
       a4 = "DE"
  elif "Pipes & Fittings" in s3_row:
       a4 = "PF"
  elif "Profiles" in s3_row:
       a4 = "PROF"
  elif "Bottles" in s3_row:
       a4 = "BTTL"
  elif "Wire and Cable" in s3_row:
       a4 = "WC"
  elif "Profiles & Tubes" in s3_row:
       a4 = "PT"
  elif "Flooring" in s3_row:
       a4 = "FL"
  elif "Coatings" in s3_row:
       a4 = "CO"
  elif "All Other" in s3_row:
       a4 = "OTHER"
  elif "Net Inventory" in s3_row:
       a4 = "INVCNG"
  elif "Construction / Building" in s3_row:
       a4 = ""
  elif "Effective Capacity" in s3_row:
       a4 = "NPC"
  elif "Effective Operating Rate (%)" in s3_row:
       a4 = "OPRT"
  elif "PET(PTA)" in s3_row:
       a4 = "PTA"
  elif "PET(Chip)" in s3_row:
       a4 = "CHIP"
  elif "Recycle production" in s3_row:
       a4 = "REPRD"
  elif "A-PET/C-PET/Other" in s3_row:
       a4 = "ACO"
  elif "Bottle Grade Resin" in s3_row:
       a4 = "BGR"
  elif "Balance" in s3_row:
       a4 = "BAL"

  else: pass

  s2_row = row[2]
  if "QUARTERLY" in row[2]:
   a3 = "QUARTERLY"
  elif "MONTHLY" in row[2]:
    a3 = "QUARTERLY.FORECAST"

 CATEGORY ="IHS_CH_SUP_DEM"
 TEMPLATE ="IHS_CH"

 TIMEZONE = "CET"
 SUPPLIERCD = "IHS"
 SUPPLIERDESC = "IHS"
 HUBCD = "EU"
 HUBDESC = "Europe"
 PERIODCD = 'SPOT'

 PRODUCTCD = "CH"
 PRODUCTDESC = "CHEMICALS"
 COMMODITY = "CHEMICALS"

 print("EU.CH.IHS." + a1 + "_" + a4 + "_" + a2+"."+a3+ "        "+CATEGORY+ "        "+TEMPLATE+ "        "+TIMEZONE+ "        "+SUPPLIERCD+ "        "+SUPPLIERDESC+ "        "+HUBCD+ "        "+HUBDESC+ "        "+PERIODCD+ "        "+PRODUCTCD+ "        "+PRODUCTDESC+"      "+COMMODITY)
