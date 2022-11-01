x=log10(t*1e-3);
y=5/2*log10(r)-x;
plot(x,y,'+')
xlabel('log10(t)');
ylabel('5/2*1og10(r)-log10(t)');
c=mean(y)
hold on;
plot(x,c,'.-') ;
hold off;
rou0=1.29;
e=rou0*10^(2*c)
kiloton=e/4.184e12