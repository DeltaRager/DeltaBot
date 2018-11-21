
const Discord = require("discord.js");
const TOKEN ='NTE0NzI2NjE3OTU2ODc2Mjg4.DtbLOQ.BavAr4UNQQy__5gdnrHzEKYL8aw';
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
