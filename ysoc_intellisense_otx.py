
from ysoc_intellisense_imports import configvars, pd,np, requests, logger, time, OTXv2, IndicatorTypes


def get_report_from_otx_db(otx_api_keys_string, get_ip_scores, report_input):
    try:
        otx_api_response_df = pd.DataFrame()
        # pdb.set_trace()
        def iterate_by_api_key(api_key):
            try:
                # pdb.set_trace()

                api_response_df = pd.DataFrame()
                if report_input == 'IP_Address':
                    otx_server_url = 'https://otx.alienvault.com/api/v1/indicators/IPv4/'
                elif report_input == 'HASH_Output':
                    otx_server_url = 'https://otx.alienvault.com/api/v1/indicators/file/'
                elif report_input == 'URL_Output':
                    otx_server_url = 'https://otx.alienvault.com/api/v1/indicators/domain/'


                headers = {'X-OTX-API-KEY': str(api_key)}
                response = requests.get(
                    otx_server_url + get_ip_scores + '/general', headers=headers,verify=False)

                # otx = OTXv2(api_key)
                # otx = OTXv2(api_key, server=otx_server)
                # result = otx.get_indicator_details_by_section(
                #     IndicatorTypes.IPv4, get_ip_scores, 'general')
                # Get all the indicators associated with a pulse
                # indicators = otx.get_pulse_indicators(get_ip_scores)
                # for indicator in indicators:
                #     print(indicator["indicator"] + indicator["type"])
                # Get everything OTX knows about google.com
                # otx.get_indicator_details_full(
                #     IndicatorTypes.IPv4, get_ip_scores)
                if response.status_code == 200:
                    try:
                        result = response.json()
                        # if report_input == 'IP_Address':
                             ## add the field name wrt too INDIpiendent applications
                        verdict = result.get('verdicts')
                        pulse_count = result['pulse_info']['count'] if 'pulse_info' in result else 0
                        api_response_df[report_input] = [get_ip_scores]
                        api_response_df['OTX_Verdicts'] = [
                            verdict]
                        api_response_df['OTX_Pulse_Count'] = [pulse_count]
                        api_response_df['OTX_Remarks'] = ["None."]
                            
                        # elif report_input == 'HASH_Output':
                        #     verdict = result.get('verdicts')
                        #     # otx_verdict = ['Malicious' for verdict in verdicts if 'malware' in verdict ]
                        #     pulse_count = result['pulse_info']['count'] if 'pulse_info' in result else 0
                        #     api_response_df[report_input] = [get_ip_scores]
                        #     api_response_df['OTX_Verdicts'] = [
                        #         verdict]
                        #     api_response_df['OTX_Pulse_Count'] = [pulse_count]
                        #     api_response_df['OTX_Pulse_Name'] = [result["pulse_info"]["pulses"][0]["name"]]
                        #     api_response_df['OTX_Description'] = [result["pulse_info"]["pulses"][0]["description"]]
                        #     api_response_df['OTX_Tags'] = [result["pulse_info"]["pulses"][0]["tags"]] #####verdict is not coming
                        #     api_response_df['OTX_Remarks'] = ["None."]

                        # elif report_input == 'URL_Output':
                        #     verdict = result.get('verdicts')
                        #     # otx_verdict = ['Malicious' for verdict in verdicts if 'malware' in verdict ]
                        #     pulse_count = result['pulse_info']['count'] if 'pulse_info' in result else 0
                        #     api_response_df[report_input] = [get_ip_scores]
                        #     api_response_df['OTX_Verdicts'] = [
                        #         verdict]
                        #     # api_response_df['OTX_Indicator'] = [result["indicator"]]
                        #     api_response_df['OTX_Pulse_Count'] = [pulse_count]
                        #     # api_response_df['OTX_Pulse_Count'] = [result["pulse_info"]["count"]] #####verdict is not coming
                        #     api_response_df['OTX_Remarks'] = ["None."]
                        
                        return api_response_df

                    except Exception as e:
                            api_response_df['OTX_Remarks'] = [e]
                            logger.exception(
                                "Error unpacking response from OTX :%s",e)

            except Exception as e:
                api_response_df['OTX_Remarks'] = [str(e)]
                logger.error(
                    'Error at iterate_by_api_key function while connecting to OTX database : ' + str(e))

        otx_api_keys_list = otx_api_keys_string.split(":,:")

        otx_api_response_df = iterate_by_api_key(otx_api_keys_list[0])
        # otx_api_response_df = pd.DataFrame()
        while otx_api_response_df.empty:
            otx_api_keys = iter(otx_api_keys_list)
            otx_api_key = next(otx_api_keys)
            if otx_api_key == otx_api_keys_list[-1:][0]:
                otx_api_response_df = iterate_by_api_key(
                    otx_api_keys_list[-1:][0])
            # otx_api_key = np.random.choice(np.array(otx_api_keys_list))
                if otx_api_response_df.empty:
                # print("OTX API Key used for IP: ",get_ip_scores,"to get threat intel score is\n",otx_api_key)
                # otx_api_response_df = iterate_by_api_key(
                #     otx_api_key)
                # # print(otx_api_response_df)
                # if otx_api_response_df["OTX_Remarks"][0] != "None.":
                    otx_api_response_df[report_input] = [
                        get_ip_scores]
                    otx_api_response_df['OTX_Remarks'] = [
                        "Unable to fetch Score's with available API Key's."]
            else:
                otx_api_response_df = iterate_by_api_key(otx_api_key)
        return otx_api_response_df
    except Exception as e:
        logger.error(
            "Got error in get_report_from_otx_db function with error:%s.", e)


def otx_db_wrapper(get_all_ip_scores, report_input):
    try:
        # pdb.set_trace()

        # print("\n OTX Report Start:")

        otx_api_results = pd.DataFrame()
        api_results_df = get_all_ip_scores
        otx_api_keys_string = configvars.data['OTX_API_KEY']  # .split(":,:")
        get_report_list = get_all_ip_scores[report_input].to_list()
        for report_value in get_report_list:
            # time.sleep(2)
            otx_api_results = otx_api_results.append(
                get_report_from_otx_db(otx_api_keys_string, report_value, report_input), ignore_index=True)
        # find elements in api_results_df that are not in otx_api_results
        if not otx_api_results.empty:
            unfetched_reports = api_results_df[~(api_results_df[report_input].isin(
                otx_api_results[report_input]))].reset_index(drop=True)

            for row in unfetched_reports.itertuples(index=True, name='Pandas'):
                missed_report = pd.DataFrame()
                missed_report[report_input] = [row[1]]
                missed_report['OTX_Remarks'] = [
                    "Unable to fetch Score's from OTX DB by YSOC Intellisense Tool."]
                otx_api_results = otx_api_results.append(
                    missed_report, ignore_index=True)

        # print(otx_api_results)
        # print("\n OTX Report End:")

        return otx_api_results
    except Exception as e:
        logger.error(
            "Got error in otx_db_wrapper function with error:%s.", e)
