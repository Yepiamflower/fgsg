# FlowerAI Discord Bot Setup

## Instructions to Set Up and Run the FlowerAI Discord Bot with Ollama

### Prerequisites
1. **Node.js**: Ensure you have Node.js installed. You can download it from [nodejs.org](https://nodejs.org/).
2. **Discord Account**: Create a Discord account if you don't have one.
3. **Ollama**: Install Ollama. Follow the installation instructions from [ollama.com](https://ollama.com/).

### Steps to Set Up
1. **Clone the Repository**:  
   Open your terminal and run:
   ```bash
   git clone https://github.com/Yepiamflower/fgsg.git
   cd fgsg
   ```

2. **Install Dependencies**:  
   Run the following command to install all required packages:
   ```bash
   npm install
   ```

3. **Configure the Bot**:  
   Create a `.env` file in the root of the project and add your Discord bot token:
   ```bash
   DISCORD_TOKEN=your_bot_token
   ```

4. **Run the Bot**:  
   Start the bot with the following command:
   ```bash
   node bot.js
   ```

### Running with Ollama
1. Make sure you have Ollama running in the background. 
2. The bot will connect to your specified Ollama model.

For any issues or contributions, feel free to create an issue or pull request on this repository. 

Happy coding!