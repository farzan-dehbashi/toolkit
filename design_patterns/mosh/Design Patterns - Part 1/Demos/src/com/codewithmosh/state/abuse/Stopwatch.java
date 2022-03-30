package com.codewithmosh.state.abuse;

public class Stopwatch {
  private State currentState = new StoppedState(this);

  public void click() {
    currentState.click();
  }

  public State getCurrentState() {
    return currentState;
  }

  public void setCurrentState(State currentState) {
    this.currentState = currentState;
  }
}
