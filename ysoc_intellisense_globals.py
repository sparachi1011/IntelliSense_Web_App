ysoc_intellisense_threatintel_dbs = {
    "ysoc_intellisense_threatintel_dbs_for_IP": {

        "abuse_cols": ["Abuse_Confidence_Score", "Abuse_Total_Reports",
                       "Abuse_Last_Reported_At", "Abuse_Remarks"],
        "vt_cols": ["Virus_Total_No_of_Databases_Checked", "Virus_Total_No_of_Reportings",
                    "Virus_Total_Average_Score", "Virus_Total_Report_Link",
                    "Virus_Total_Remarks"],
        "otx_cols": ["OTX_Verdicts", "OTX_Pulse_Count", "OTX_Remarks"]},

    "ysoc_intellisense_threatintel_dbs_for_hash_url": {

        "vt_cols": ["Virus_Total_No_of_Databases_Checked", "Virus_Total_No_of_Reportings",
                    "Virus_Total_Average_Score",
                    "Virus_Total_Remarks"],
        "otx_cols": ["OTX_Verdicts", "OTX_Pulse_Count", "OTX_Remarks"]},

    # "ysoc_intellisense_threatintel_dbs_for_url": {

    #     "vt_cols": ["Virus_Total_No_of_Databases_Checked", "Virus_Total_No_of_Reportings",
    #                 "Virus_Total_Average_Score",
    #                 "Virus_Total_Remarks"],
    #     "otx_cols": ["OTX_Verdicts", "OTX_Pulse_Count", "OTX_Remarks"]},  # "OTX_Pulse_Name", "OTX_Description","OTX_Tags",

    "ip_void_cols": [],
    "cisco_talos_cols": [],
    "bad_ips_cols": [],
    "my_ips_cols": [],
    "hibp_cols": [],
    "url_scan_cols": []

}

# ysoc_intellisense_threatintel_dbs = {
#     "ysoc_intellisense_threatintel_dbs_for_IP": {

#         "abuse_cols": ["Abuse_Confidence_Score", "Abuse_Total_Reports",
#                        "Abuse_Last_Reported_At", "Abuse_Remarks"],
#         "vt_cols": ["Virus_Total_No_of_Databases_Checked", "Virus_Total_No_of_Reportings",
#                     "Virus_Total_Average_Score", "Virus_Total_Report_Link",
#                     "Virus_Total_Remarks"],
#         "otx_cols": ["OTX_Verdicts", "OTX_Pulse_Count", "OTX_Remarks"]},

#     "ysoc_intellisense_threatintel_dbs_for_hash": {

#         "vt_cols": ["Virus_Total_No_of_Databases_Checked", "Virus_Total_No_of_Reportings",
#                     "Virus_Total_Average_Score",
#                     "Virus_Total_Remarks"],
#         "otx_cols": ["OTX_Verdicts", "OTX_Pulse_Count", "OTX_Remarks"]},

#     "ysoc_intellisense_threatintel_dbs_for_url": {

#         "vt_cols": ["Virus_Total_No_of_Databases_Checked", "Virus_Total_No_of_Reportings",
#                     "Virus_Total_Average_Score",
#                     "Virus_Total_Remarks"],
#         "otx_cols": ["OTX_Verdicts", "OTX_Pulse_Count", "OTX_Remarks"]},  # "OTX_Pulse_Name", "OTX_Description","OTX_Tags",

#     "ip_void_cols": [],
#     "cisco_talos_cols": [],
#     "bad_ips_cols": [],
#     "my_ips_cols": [],
#     "hibp_cols": [],
#     "url_scan_cols": []

# }


# columns_to_render_in_html = ["UserName",
#                              "IP_Address",
#                              "YSOC_IntelliSense_Verdict",
#                              "Abuse_Confidence_Score",
#                              "Virus_Total_Average_Score",
#                              "OTX_Verdicts", "OTX_Pulse_Count"]

columns_to_render_in_html = {"columns_to_render_for_IP": ["UserName",
                                                          "IP_Address",
                                                          "YSOC_IntelliSense_Verdict",
                                                          "Abuse_Confidence_Score",
                                                          "Virus_Total_Average_Score",
                                                          "OTX_Verdicts", "OTX_Pulse_Count"],
                             "columns_to_render_for_Hash": ["UserName",
                                                            "HASH_Output",
                                                            "YSOC_IntelliSense_Verdict",
                                                            "Virus_Total_Average_Score",
                                                            "OTX_Verdicts", "OTX_Pulse_Count"],
                             "columns_to_render_for_URL": ["UserName",
                                                           "URL_Output",
                                                           "YSOC_IntelliSense_Verdict",
                                                           "Virus_Total_Average_Score",
                                                           "OTX_Verdicts", "OTX_Pulse_Count"]}

