package ex0.algo;

import ex0.Building;
import ex0.CallForElevator;
import ex0.Elevator;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class algorithm implements ElevatorAlgo {

    private Building building;
    private ArrayList<CallForElevator>[] calls;



    @Override
    public Building getBuilding() {
        return this.building;
    }

    @Override
    public String algoName() {
        return "Online destination dispatch elevator algorithm";
    }

    @Override
    public int allocateAnElevator(CallForElevator c) {

        return 0;
    }

    @Override
    public void cmdElevator(int elev) {

    }
}
