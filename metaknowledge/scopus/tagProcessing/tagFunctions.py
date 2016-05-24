def commaSpaceSeperated(val):
    return val.split(', ')

def semicolonSpaceSeperated(val):
    return val.split('; ')

def semicolonSeperated(val):
    return val.split(';')

def stringValue(val):
    return val

def integralValue(val):
    print(val)
    return int(val)

scopusTagToFunction = {
    'Authors' : commaSpaceSeperated,
    'Title' : stringValue,
    'Year' : integralValue,
    'Source title' : stringValue,
    'Volume' : stringValue,
    'Issue' : stringValue,
    'Art. No.' : stringValue,
    'Page start' : stringValue,
    'Page end' : stringValue,
    'Page count' : integralValue,
    'Cited by' : integralValue,
    'DOI' : stringValue,
    'Link' : stringValue,
    'Affiliations' : stringValue,
    'Authors with affiliations' : semicolonSpaceSeperated,
    'Abstract' : stringValue,
    'Author Keywords' : semicolonSpaceSeperated,
    'Index Keywords' : semicolonSpaceSeperated,
    'Molecular Sequence Numbers' : stringValue,
    'Chemicals/CAS' : stringValue,
    'Tradenames' : semicolonSpaceSeperated,
    'Manufacturers' : semicolonSpaceSeperated,
    'Funding Details' : semicolonSpaceSeperated,
    'References' : semicolonSpaceSeperated,
    'Correspondence Address' : semicolonSpaceSeperated,
    'Editors' : stringValue,
    'Sponsors' : semicolonSeperated,
    'Publisher' : stringValue,
    'Conference name' : stringValue,
    'Conference date' : stringValue,
    'Conference location' : stringValue,
    'Conference code' : integralValue,
    'ISSN' : stringValue,
    'ISBN' : semicolonSpaceSeperated,
    'CODEN' : stringValue,
    'PubMed ID' : stringValue,
    'Language of Original Document' : semicolonSpaceSeperated,
    'Abbreviated Source Title' : stringValue,
    'Document Type' : stringValue,
    'Source' : stringValue,
    'EID' : stringValue,

}
