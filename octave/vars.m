function [x, y, z, class, a, b, theta] = vars(yy, pass)
    z = 19;
    x = yy * z;
    y = yy / z;
    theta = linspace(0,2*pi,100);
    a = cos(theta);
    b = sin(theta);
    class = class(pass);
end
