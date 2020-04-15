const Discord = require('discord.js');
const bot = new Discord.Client();
	
	const token = //token;
	const PREFIX ='!';



	bot.on('ready', ()=>{
		console.log('This bot is online!');
	})

		bot.on('message',message=>{

			let args = message.content.substring(PREFIX.length).split(" "); 

			switch(args[0]){
				case 'scrimsetup':
				message.reply('sirfscrimlik	!');
				break;
				case 'scrim':
				if(args[1] === 'setup')
				{
					message.reply('Enter the names');	
				}
				else{
					message.chanel.sendMessage('Input to sahi dede bhai xd')
				}
				break;
			} 
		})
	bot.login(token);
