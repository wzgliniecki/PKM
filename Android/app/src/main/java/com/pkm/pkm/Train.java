package com.pkm.pkm;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.List;

/**
 * Created by Karol on 26.10.2017.
 */

public class Train{
    private int id;
    private String device_type;
    private int velocity;
    private int train_identificator;

    public Train(int id, String device_type, int velocity, int train_identificator) {
        this.id = id;
        this.device_type = device_type;
        this.velocity = velocity;
        this.train_identificator = train_identificator;
    }

    public int getVelocity() {
        return velocity;
    }

    public void setVelocity(int velocity) {
        this.velocity = velocity;
    }

    public int getTrain_identificator() {
        return train_identificator;
    }

    public void setTrain_identificator(int train_identificator) {
        this.train_identificator = train_identificator;
    }

}