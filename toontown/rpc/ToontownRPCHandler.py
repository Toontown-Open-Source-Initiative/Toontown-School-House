class ToontownRPCHandler:
    def __init__(self, air):
        self.air = air

    def rpc_ping(self, data):
        """
        Summary:
            Responds with the provided [data]. This method exists for testing
            purposes.

        Parameters:
            [any data] = The data to be given back in response.

        Example response: 'pong'
        """
        return data

    # Website
    def rpc_cr_get_rewards(self, request):
        """
        Summary:
            Responds with the Award Choices allowed for Code Redemption.
            Used when CREATE-LOT page loads

        Example response: [1: [100, 150]]
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCGetAwardChoices(request)
        return request

    def rpc_cr_check_for_current_lots(self, request):
        """
        Summary:
            Responds with TRUE or FALSE based on if there are pre-existing
            lots for code redempion.

        Example response: 
            'true'
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCCheckForLots(request)
        return request

    def rpc_cr_get_lot_names(self, request):
        """
        Summary:
            Responds with list of current code lots for code redemption.

        Example response: 
            ['testing', '1234']
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCGetLotNames(request)
        return request

    def rpc_cr_get_expiration_lot_names(self, request):
        """
        Summary:
            Responds with list of lots with expiration dates

        Example response: 
            ['testing', '1234']
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCGetLotNamesWithExpiration(request)
        return request

    def rpc_cr_create_lot(self, request, manualCode, numCodes, lotName, rewardType, rewardItemId, manualCodeStr=None, hasExpiration=False, expirationMonth=None, expirationDay=None, expirationYear=None):
        """
        Summary:
            Creates a new lot

        Parameters:
            lotName = The current lot name
            justCode = If we only want codes back or more details
            filterOption = The Filter Option 

        Example successful response: 
            {
                message: 'Code Lot NAME (FILTER), RESULT_COUNT results',
                lookupResults: [{'code': 'testing'}]
            }

        Example error response: 
            {
                errorCode: 9999,
                error: 'Unavailable'
            }
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCCreateLot(request, manualCode, numCodes, lotName, rewardType, rewardItemId, manualCodeStr, hasExpiration, expirationMonth, expirationDay, expirationYear)
        return request

    def rpc_cr_view_lot_details(self, request, lotName, justCode, filterOption):
        """
        Summary:
            Responds with lot details

        Parameters:
            lotName = The current lot name
            justCode = If we only want codes back or more details
            filterOption = The Filter Option 

        Example successful response: 
            {
                message: 'Code Lot NAME (FILTER), RESULT_COUNT results',
                lookupResults: [{'code': 'testing'}]
            }

        Example error response:
            {
                errorCode: 9999,
                error: 'Unavailable'
            }
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCViewLot(request, lotName, justCode, filterOption)
        return request

    def rpc_cr_modify_lot(self, request, lotName, expirationMonth, expirationDay, expirationYear):
        """
        Summary:
            Modify a lot to change expiration date

        Parameters:
            lotName = The current lot name
            expirationMonth = New Expiration Month
            expirationDay = New Expiration Day
            expirationYear = New Expiration Year

        Example successful response: 
            {
                message: 'Expiration date set to DATE',
                lookupResults: [{'code': 'testing'}]
            }

        Example error response: 
            {
                errorCode: 9999,
                error: 'Unavailable'
            }
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCModifyLot(request, lotName, expirationMonth, expirationDay, expirationYear)
        return request

    def rpc_cr_delete_lot(self, request, lotName):
        """
        Summary:
            Attempts to delete the given code lot

        Parameters:
            lotName = The lot name to delete

        Example successful response: {
            message: 'Code Lot LOTNAME deleted'
        }
        Example error response: {
            errorCode: 9999,
            error: 'Unavailable'
        }
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCDeleteLot(request, lotName)
        return request

    def rpc_cr_lookup(self, request, code=None, avId=None):
        """
        Summary:
            Looks up the current code lot based on code, or avatar Id

        Parameters:
            code = The code to look up (OPTIONAL)
            avId = The Avatar ID to look up (OPTIONAL)

        Example successful response: {
            message: 'Code Lookup: QUERY, RESULT_COUNT results',
            lookupResults: [{'code': 'testing'}]
        }
        Example error response: {
            errorCode: 9999,
            error: 'Unavailable'
        }
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCLookup(request, code, avId)
        return request

    def rpc_cr_redeem_code(self, request, code, avId):
        """
        Summary:
            Redeems the given code for the given avatar ID

        Parameters:
            code = The code to look up
            avId = The Avatar ID to look up

        Example successful response: {
            results: 'Redeemed code %s for avId %s, awarded [%s | %s]'
        }
        Example error response: {
            errorCode: 9999,
            error: 'Unavailable'
        }
        """
        self.air.codeRedemptionManager.rpcManager.handleRPCRedeemCode(request, code, avId)
        return request
