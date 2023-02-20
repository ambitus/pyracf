from pyracf.common.SecurityRequest import SecurityRequest


class DatasetRequest(SecurityRequest):
    def __init__(self, datasetname: str, function: str, generic: str = 'no', volid: str = '') -> None:
        super().__init__()
        self.security_definition.tag = "dataset"

        self.security_definition.attrib = {
            "name": datasetname,
            "operation": function,
            "generic": generic,
            "requestid": "DatasetRequest"
        }
        
        if not volid == '':
            self.security_definition.attrib["volid"] = volid
        if not generic == "no":
            self.security_definition.attrib["generic"] = generic