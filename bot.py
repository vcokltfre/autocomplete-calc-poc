from disnake import ApplicationCommandInteraction
from disnake.ext.commands import Bot, Param
from InfixParser import evaluate

bot = Bot(command_prefix="!")


@bot.slash_command(name="calc", description="Calculate maths equations live")
async def calc(
    ctx: ApplicationCommandInteraction,
    expr: str = Param(description="The expression to evaluate", autocomp=lambda _, value: [str(evaluate(value))]),
):
    await ctx.response.send_message("Result: " + str(evaluate(expr)))


bot.run("your_token")
