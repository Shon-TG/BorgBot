"""
GITHUB File Uploader Plugin for userbot. Heroku Automation should be Enabled. Else u r not that lazy // For lazy people
Instructions:- Set GITHUB_ACCESS_TOKEN and GIT_REPO_NAME Variables in Heroku vars First
usage:- .commit reply_to_any_plugin //can be any type of file too. but for plugin must be in .py 
By:- @Zero_cool7870 

"""


from github import Github
import aiohttp
import asyncio
import os
import time
from datetime import datetime
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
from uniborg.util import admin_cmd, humanbytes, progress, time_formatter


GIT_TEMP_DIR = "./temp/"
@borg.on(admin_cmd(pattern="delete ?(.*)", allow_sudo=True))
async def download(event):
	if event.fwd_from:
		return	
	if Config.GITHUB_ACCESS_TOKEN is None:
		await event.edit("`Please ADD Proper Access Token from github.com`") 
		return   
	if Config.GIT_REPO_NAME is None:
		await event.edit("`Please ADD Proper Github Repo Name of your userbot`")
		return 
	mone = await event.reply("Processing ...")
	input_str = event.pattern_match.group(1)
	if not os.path.isdir(GIT_TEMP_DIR):
		os.makedirs(GIT_TEMP_DIR)

async def git_commit(file_name,mone):        
	content_list = []
	access_token = Config.GITHUB_ACCESS_TOKEN
	g = Github(access_token)
	file = open(file_name,"r",encoding='utf-8')
	commit_data = file.read()
	repo = g.get_repo(Config.GIT_REPO_NAME)
	print(repo.name)
	create_file = True
	contents = repo.get_contents("")
	for content_file in contents:
		content_list.append(str(content_file))
		print(content_file)
	for i in content_list:
		delete_file = True
		if i == 'ContentFile(path="'+file_name+'")':
			return await mone.edit("`File Already Exists`")
			delete_file = False
	file_name = "stdplugins/"+file_name		
	if delete_file == True:
		file_name = file_name.replace("./temp/","")
		print(file_name)
		try:
			repo.delete_file(file_name, "Uploaded New Plugin", commit_data, branch="master")
			print("Committed File")
			await mone.edit("`File Deleted From GitHub`")
		except:
			print("Cannot Create Plugin")
			await mone.edit("Cannot Upload Plugin")
	else:
		return await mone.edit("`Committed Suicide`")


	
