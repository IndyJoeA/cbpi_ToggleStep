# Toggle Step Plugin for CraftBeerPi 3.0

This is a very simple plugin that adds a Step to CraftBeerPi called ToggleStep.  This step will turn on, turn off, or set the power on any actor, and then immediately continue with the next step.  This is useful if you have a need to turn something on like a pump, but then continue execution of other steps without turning that device back off.  Or you could turn something on and set the power, and then use another ToggleStep later to turn it back off.

## Usage
1.  Download the ToggleStep plugin from within CraftBeerPi 3.0, and then reboot your Raspberry Pi.
2.  Configure a new brewing step, and select ToggleStep as the type.
3.  Enter values for the following settings:
    1.  **Actor**: Select the Actor that you wish to control.
    2.  **Power**: If you wish to specify the Power value of the actor, enter it here. If you do not enter a Power value, the default of 100% will be used.
    3.  **Toggle Type**: Select On to turn on the Actor, select Off to turn off the Actor, or select Power Only to just change the power of the actor without changing its on/off state.
    4.  Click **Update** to save your configuration.

