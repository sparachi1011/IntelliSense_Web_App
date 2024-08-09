import os
import csv
import ipaddress
import json
import requests
import sys
import strictyaml
import pandas as pd
import numpy as np
import pdb
import time
import datetime as dt
import random

from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
from openpyxl import Workbook

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_pandas.io import read_frame
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str

from ysoc_intellisense_gui import settings
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from passlib.hash import django_pbkdf2_sha256 as handler

import logging
import warnings
warnings.filterwarnings("ignore", category=Warning)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email import message as msg

working_directory = os.getcwd() + "/"
print("Current working directory:", working_directory)


def generate_logger():
    try:
        log_file_path = working_directory + 'ysoc_intellisense_automation_logs/ysoc_intellisense_automation_logs_' + \
            str(dt.datetime.now().strftime("%Y_%m_%d")) + '.log'
        if os.path.exists(log_file_path.rsplit("/", 1)[0]):
            if os.path.exists(log_file_path):
                log_file_name = log_file_path
            else:
                log_file = open(log_file_path, 'a')
                log_file.close()
                log_file_name = log_file_path
        else:
            try:
                # # print("\n&&&&&&MakeDirectoryFromImports.py", ysoc_module_path)
                os.mkdir(log_file_path.rsplit("/", 1)[0])  # , mode=0o777)
                # os.mkdir('./execution_logs')#, mode=0o777)
                log_file = open(log_file_path, 'a')
                log_file.close()
                log_file_name = log_file_path
                # # print("\n&&&&&&AfterMakeDirectoryFromImports.py", ysoc_module_path)
            except Exception as e:
                print("Error while creating log file from imports.py\n", e)
        if log_file_name:
            try:
                log_process_activities(
                    'ysoc_intellisense_automation_logs', log_file_name)
                logger = logging.getLogger('ysoc_intellisense_automation_logs')
            except Exception as e:
                log_process_activities(
                    'ysoc_intellisense_automation_logs', log_file_path)
                logger = logging.getLogger('ysoc_intellisense_automation_logs')
        return logger
    except Exception as e:
        print("Got Error in generate_logger function as:\n", e)


def log_process_activities(logger_name, log_file, level=logging.INFO):
    """
    This Function will create a logger object.

    Parameters
    ----------
    logger_name : String
        DESCRIPTION: name of the logger object.
    log_file : String
        DESCRIPTION: Path to log file.
    logger_level : String
        DESCRIPTION: Level of logging to be tracked.

    Returns
    -------
    Logger object.

    """
    try:
        logger = logging.getLogger(logger_name)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        fileHandler = logging.FileHandler(log_file, mode='a')
        fileHandler.setFormatter(formatter)
        logger.setLevel(level)
        logger.addHandler(fileHandler)

        return logger
    except FileNotFoundError as error:
        logger.error(
            "FileNotFoundError at log_process_activities " + str(error))
    except Exception as error:
        logger.error("Error at log_process_activities " + str(error))


# def get_azure_secrets():
#     import os
#     from azure.keyvault.secrets import SecretClient
#     from azure.identity import DefaultAzureCredential

#     keyVaultName = "YSOC-Internal-Secrets"  # os.environ["KEY_VAULT_NAME"]
#     KVUri = f"https://{keyVaultName}.vault.azure.net"
#     secretName = "YSOC-Abuse-IPDB"

#     credential = DefaultAzureCredential()
#     # exclude_shared_token_cache_credential=True)
#     client = SecretClient(vault_url=KVUri, credential=credential)

#     # secretName = input("Input a name for your secret > ")
#     # secretValue = input("Input a value for your secret > ")

#     # print(
#     #     f"Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ...")

#     # client.set_secret(secretName, secretValue)

#     # print(" done.")

#     print(f"Retrieving your secret from {keyVaultName}.")
#     retrieved_secret = client.get_secret(secretName)
#     print(f"Retrieved your secret from {keyVaultName}.")
#     # print(f"Your secret is '{retrieved_secret.value}'.")
#     # print(f"Deleting your secret from {keyVaultName} ...")

#     # poller = client.begin_delete_secret(secretName)
#     # deleted_secret = poller.result()

#     return retrieved_secret.value


def load_config_yaml():
    try:
        f = open("integrated_database_search/config.yaml", "r")
        configvars = strictyaml.load(f.read())
        f.close()
        return configvars
    except FileNotFoundError:
        print("Config.yaml not found. Check the example config file and rename to 'config.yaml'.")


logger = generate_logger()
# ysoc_secrets = json.loads(get_azure_secrets())
# ysoc_secrets = {'ysoc_abuse_ipdb_script': {'elastic_creds': {'global-threatintel-abuseipdb': '4LiJ88frD%ipDB',
#                                                              'abuse_ipdb_api_key': '0c487dc08176e92b8bbf018506add8c0a1e252a3d913071140ca602668aaa6008a755813c876265b'}}}
configvars = load_config_yaml()
# print(configvars.data['AB_API_KEY'])
