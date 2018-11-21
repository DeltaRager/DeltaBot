
const Discord = require("discord.js");
const TOKEN = process.env.token;
const bot = new Discord.Client();





 bot.on("ready", async ()=>
{
  console.log(`DeltaBot is online!`);
}

);

bot.on('message',function(message){
  if(message.content =='hello')
  {
    message.channel.sendMessage('Hey ' + message.author + ' , die');
  }
});

bot.login(TOKEN);
