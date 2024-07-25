using Godot;
using System;
using Location;

public class Player : Node
{
	//this is all lovely but I already have a Player.tscn
	public Location loc;
	public Page page;
	public Player(Location l){
		loc = l;
		page = new Page(this);
	}
}
